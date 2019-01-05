from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from flask.json import jsonify
from config import ProductionConfig
from forms import BidForm
from utils import send_email


app = Flask(__name__)
app.config.from_object(ProductionConfig)

csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers')
def customers():
    return render_template('customers.html')


@app.route('/bids', methods=['POST'])
def bids():
    return request.body


@app.route('/test', methods=['GET'])
def test():
    form = BidForm()
    return render_template('test.html', form=form)


@app.route('/ajax', methods=['POST'])
def ajax():
    form = BidForm()

    if form.validate_on_submit():
        send_email(
            name=form.name.data,
            phone=form.phone.data,
            message=form.message.data
        )
        return send_json_response({'message': 'Ваша заявка успешно отправлена'}, 200)

    return send_json_response(form.errors, 400)


def send_json_response(message, status_code):
    response = jsonify(message)
    response.status_code = status_code
    return response