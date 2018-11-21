from datetime import datetime


def criar_mensagem(nome, email, texto):

    msg_texto = '\n-----INÍCIO DA MENSAGEM******\n'
    msg_texto += 'Nome: ' + nome + ' | ' + 'Email: ' + email + '\n'
    msg_texto += 'Em: ' + str(datetime.now()) + '\n'
    msg_texto += '\n\nMensagem:\n' + texto + '\n'
    # msg_texto += '\nResposta do ReCaptcha: ' + str(respReCaptcha)
    msg_texto += '\n--------FIM DA MENSAGEM--------\n'
    return msg_texto
