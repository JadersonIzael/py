from flask import Flask, render_template
import requests

app = Flask(__name__)

#1 pagina do site
# colocar no ar
# route -> qual o link da pagina
# função -> o q sera exibido na pagina


@app.route("/home")
def homepage():
    return render_template("homepage.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios/")
def cadastro():
    return render_template("cadastroUsuarios.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)

@app.route("/cotacao/<cotacao>")
def cotacao(cotacao):
    moeda = pegar_cotacao(cotacao)
    cotacao = f"O valor do {cotacao} hoje é de R$: {moeda}"
    return render_template("cotacao.html", cotacao = cotacao)

def pegar_cotacao(moeda):
    link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
    return cotacao

if __name__ == "__main__":
    app.run(debug=True)