# Run with "python server.py"
from bottle import run, get, post, request
from api.views import list_notes, add_notes, login_jwt
from api.tools import token_required
# Start your code here, good luck (: ...

# Index API
@get('/')
def index():
    return "Hello World!, This is API Notes Basic."

# Servicio Login
@post('/login/')
def login():
    return login_jwt(request)

# Servicio Listar Notas
@get('/notes/')
@token_required
def get_notes():
    return list_notes(request)

# Servicio Agregar una Nota
@post('/notes/')
@token_required
def post_notes():
    return add_notes(request)

run(host='localhost', port=8000)
