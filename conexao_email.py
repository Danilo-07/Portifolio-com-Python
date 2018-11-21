from flask_mail import Mail, Message
from smtplib import SMTPException, SMTPServerDisconnected
from smtplib import SMTPAuthenticationError
import configs_site as cfs


# iniciar conexão
def enviar_email(app, msg_texto, nome):
    # configuracoes para gmail
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = cfs.email
    app.config['MAIL_PASSWORD'] = cfs.senha

    # criando o objeto email
    mail = Mail(app)

    assunto = 'Mensagem de SitePessoal - O {} enviou uma mensagem'.format(nome)

    # criando a mensagem
    msg = Message(assunto, sender=cfs.email, recipients=[
        cfs.destino])
    msg.body = msg_texto

    # emviando a mensagem
    try:
        resposta_email = True
        mail.send(msg)
    except SMTPAuthenticationError:
        resposta_email = False
    except SMTPServerDisconnected:
        resposta_email = False
    except SMTPException:
        resposta_email = False

    return resposta_email
