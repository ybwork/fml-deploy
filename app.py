from flask import Flask, render_template
from config import ProductionConfig
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(ProductionConfig)

@app.route('/')
def hello():
    mail = Mail(app)
    msg = Message(
    	'Hello', 
    	sender='kaduk9393@gmail.com',
    	recipients=['costilek@gmail.com']
    )
    msg.body = 'testing'
    msg.html = '<b>testing</b>'
    mail.send(msg)
    return 'Hi'