#Importar bibliotecas necessárias
from flask import Flask, render_template

# Criar aplicativo Flask
app = Flask(__name__)

# Definir rotas para as páginas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

# Executar aplicativo
if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=3000))
