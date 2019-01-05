from flask import current_app as app
from flask_mail import Mail, Message


def send_email(name, phone, message):
    mail = Mail(app)
    msg = Message(
        'Заявка с сайта', 
        sender='kaduk9393@gmail.com',
        recipients=['costilek@gmail.com']
    )
    msg.body = 'yess'
    msg.html = '''
                <p>Имя: {name}</p>
                <p>Телефон: {phone}</p>
                <p>Сообщение: {message}</p>
                '''.format(
                        name=name,
                        phone=phone,
                        message=message if message else '...'
                    )
    return mail.send(msg)
