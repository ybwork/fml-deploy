from flask import current_app as app
from flask_mail import Mail, Message


def send_mail():
    mail = Mail(app)
    msg = Message(
        'Hello', 
        sender='kaduk9393@gmail.com',
        recipients=['costilek@gmail.com']
    )
    msg.body = 'testing'
    msg.html = '<b>testing</b>'
    return mail.send(msg)
