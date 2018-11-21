from flask import Flask, render_template, request, url_for
import conexao_email
import mensagem_texto
import validacao
import leitorjson
import configs_site as cfs

app = Flask(__name__)
app.secret_key = '65#9DMN_T'


# rota para apresentar a página inicial
@app.route('/')
def index():
    return render_template('index.html', templatecss='css/index.css',
                           nome=cfs.nome_pessoal)


# rota para apresentar a página com o curriculum
@app.route('/curriculum')
def curriculo():
    return render_template('curriculum.html', templatecss='css/curriculum.css')


# rota para apresentar a página com o portifólio
@app.route('/projetos')
def projeto():
    return render_template('projetos.html', templatecss='css/projetos.css')


# rota para apresentar a página com o formulário de contato
@app.route('/contato')
def contato():
    return render_template('contato.html', templatecss='css/contato.css',
                           site_key=cfs.site_key)


# rota para receber mensagem enviada na rota /contato
# pelo metodo post com AJAX
@app.route('/mensagem', methods=['POST', ])
def enviar_mensagem():
    nome = request.form['nome']
    email = request.form['email']
    texto = request.form['mensagem']
    respReCaptcha = request.form['g-recaptcha-response']

    nome_email_ok = validacao.validar_nome_email(nome, email)
    if (nome_email_ok):

        recaptcha_ok = validacao.validar_recaptcha(respReCaptcha)
        if (recaptcha_ok):

            msg_texto = mensagem_texto.criar_mensagem(nome, email, texto)
            if conexao_email.enviar_email(app, msg_texto, nome):
                return ('', 200)
            else:
                return ('Erro com o servidor de Email', 500)
        else:
            return ('Erro com o Google ReCaptha', 403)
    else:
        return ('Erro ao enviar nome e/ou email', 400)


creditos = 'Desenvolvido por <a href="https://github.com/Danilo-07" target="_blank">Danilo Moreira</a>'

app.run(host='0.0.0.0', debug=True)
