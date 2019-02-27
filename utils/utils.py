from utils.settings import SECRET_KEY
from datetime import datetime
import urllib.request
import json
import re  # RegEx

def name_and_email_validation(nome, email):
    nome_regex = "[A-ZÀ-Ÿa-zà-ÿ ']{4,}"
    email_regex = "[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+"
    validou = re.match(nome_regex, nome) and re.match(
        email_regex, email.lower())
    return validou


def recaptcha_validation(response):
    url = 'https://www.google.com/recaptcha/api/siteverify?'
    url = url + 'secret=' + str(SECRET_KEY)
    url = url + '&response=' + str(response)

    resultado = json.loads(urllib.request.urlopen(url).read())
    return resultado['success']


def create_email_message(nome, email, texto):

    msg_texto = '\n-----INÍCIO DA MENSAGEM******\n'
    msg_texto += 'Nome: ' + nome + ' | ' + 'Email: ' + email + '\n'
    msg_texto += 'Em: ' + str(datetime.now()) + '\n'
    msg_texto += '\n\nMensagem:\n' + texto + '\n'
    # msg_texto += '\nResposta do ReCaptcha: ' + str(respReCaptcha)
    msg_texto += '\n--------FIM DA MENSAGEM--------\n'
    return msg_texto
