from flask import Flask
from routes.home import home_route
from routes.cliente import client_route

#Inicialização deve estar no topo e o métod run no final
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix='/clientes')


#Método run
app.run(debug=True)