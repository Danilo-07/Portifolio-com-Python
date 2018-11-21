import re  # RegEx
import json
import urllib.request
import configs_site as cfs

secretkey = cfs.secret_key


def validar_nome_email(nome, email):
    nome_regex = "[A-ZÀ-Ÿa-zà-ÿ ']{4,}"
    email_regex = "[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+"
    validou = re.match(nome_regex, nome) and re.match(
        email_regex, email.lower())
    return validou


def validar_recaptcha(response):
    url = 'https://www.google.com/recaptcha/api/siteverify?'
    url = url + 'secret=' + str(secretkey)
    url = url + '&response=' + str(response)

    resultado = json.loads(urllib.request.urlopen(url).read())
    return resultado['success']
