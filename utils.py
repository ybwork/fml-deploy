from flask import current_app as app
from flask_mail import Mail, Message


def send_mail(message, recipient):
	mail = Mail(app)
    msg = Message(
        'Заявка с сайта', 
        sender='kaduk9393@gmail.com',
        recipients=[recipient]
    )
    msg.body = 'yess'
    msg.html = '<b>{}</b>'.format(message)
    return mail.send(msg)
