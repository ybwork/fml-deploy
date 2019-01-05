from flask_wtf import FlaskForm
from flask import current_app as app
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


csrf = CSRFProtect(app)


class BidForm(FlaskForm):
    name = StringField(
        'name',
        validators=[
            DataRequired('Заполните имя'),
            Length(max=100, message='Превышен лимит символов')
        ]
    )
    phone = StringField(
        'phone',
        validators=[
            DataRequired('Заполните телефон'),
            Length(max=20, message='Превышен лимит символов')
        ],

    )
    message = TextAreaField('message')
