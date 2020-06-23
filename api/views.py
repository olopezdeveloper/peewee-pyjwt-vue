from api.models import Note, User
from api.serializers import NoteSchema
from api.settings_secret import SECRET_KEY
from playhouse.shortcuts import model_to_dict
from bottle import HTTPResponse
import jwt
import datetime
import json

# Proceso de logeo y generar JWT
def login_jwt(request):
    """
        username: required
        password: required
    """
    data = json.loads(request.body.read().decode('utf-8'))
    username = data['username']
    password = data['password']

    try:
        user = User.get(User.username == username, User.password == password)
    except Exception as e:
        # Si usuario no existe retornamos 401
        print("User do not exist")
        print(e)
        return HTTPResponse({'WWW-Authenticate': 'Basic realm="Login Required"'}, status=401)

    token = jwt.encode({
            'id': user.id,
            'user': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY)

    return HTTPResponse({'token': token.decode('UTF-8')}, status=200)

def list_notes(request):
    notes = Note.select().where(Note.user == request.user.id)
    schema = NoteSchema(many=True)

    result = schema.dump(list(notes))
    return HTTPResponse({'results': result.data}, status=200)


def add_notes(request):
    """
        text: required
    """
    data = json.loads(request.body.read().decode('utf-8'))

    if 'text' not in data or data['text'] == '' or not data['text']:
        return HTTPResponse({'text': 'required'}, status=400)
    
    if len(data['text']) > 1024:
        return HTTPResponse({'text': 'string can not be greater than 1024 characters'},
                             status=400)

    text = data['text']
    user_id = request.user.id

    note = Note(user=user_id, text=text)
    note.save()
    schema = NoteSchema()
    result = schema.dump(model_to_dict(note))  # Serializamos el objeto creado

    return HTTPResponse(result.data, status=201)
