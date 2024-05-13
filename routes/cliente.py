from flask import Blueprint, render_template

client_route = Blueprint('cliente', __name__)

"""
Rota de Clientes

    - /clientes/ {GET} - Listar os clientes
    - /clientes/ {POST} - Inserir o cliente no servidor
    - /clientes/new {GET} - Renderizar o formulário para criar um cliente
    - /clientes/<id> {GET} - Obter os dados de um cliente
    - /clientes/<id>/edit {GET} - Renderizar um formulário para editar os dados de um cliente
    - /clientes/<id>/update {PUT} - Atualizar os dados de um cliente
    - /clientes/<id>/delete {DELETA} - Deleta um registro do usuário
    
"""


@client_route.route('/')
def lista_clientes():
    """Listar os clientes"""
    return {'pagina': "lista_clientes"}

# Rota dinamica
@client_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir os dados do cliente"""
    pass

# Por padrão é GET
@client_route.route('/new')
def form_cliente():
    """Formulário para cadastrar um cliente"""
    return {'pagina': "formulario clientes"}

@client_route.route('/<int:client_id>')
def detalhe_cliente(client_id):
    """Exibir detalhes do cliente"""
    pass

@client_route.route('/<int:client_id>/edit')
def form_edit_cliente(client_id):
    """Formulário para editar um cliente"""
    pass

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def atualizar_cliente(client_id):
    """Atualizar informações do cliente"""
    pass

@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def deletar_cliente(client_id):
    """Deletar informações do cliente"""
    pass