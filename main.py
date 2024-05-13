from flask import Flask, url_for, render_template


#Inicialização deve estar no topo e o métod run no final
app = Flask(__name__)


#Rotas
@app.route("/")
def index():
    titulo = "Gestão de Usuários"
    usuarios = [
        {'nome': 'Samuel', 'membro_ativo': True},
        {'nome': 'Pedro', 'membro_ativo': False}
    ]

    return render_template('index.html', titulo=titulo, usuarios = usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """
        <br>
        <p>Assista mais vídeo aulas no canal <a href="https://www.youtube.com/@jrsistemas9373">JRPDV</a></p>
        """


#Método run
app.run(debug=True)