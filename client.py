# Run with "python client.py"
from bottle import get, run, static_file, post, request, route
from web.ajax_service import ajax_service

# Pagina principal
@get('/')
def index():
    return static_file('index.html', root="web/template/")

# Listar Notas
@get('/notes/')
def notes():
    return static_file('notes.html', root="web/template/")

# Generico servicio para todo Ajax
@post('/ajax-service/')
def ajax():
    return ajax_service(request)

# Servir archivos estaticos
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host='localhost', port=5000)
