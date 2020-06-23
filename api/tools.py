# Utils functions for all the API
from bottle import request
from api.settings_secret import SECRET_KEY
from api.models import User
from functools import wraps
from bottle import HTTPResponse
import jwt

# Validador JWT Decorador
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')

        if not token:
            return HTTPResponse({'message': 'Token is missing!'}, status=401)

        # Validacion del JWT
        try:
            data = jwt.decode(token, SECRET_KEY)
        except Exception as e:
            print(e)
            return HTTPResponse({'message': 'Token is invalid!'}, status=401)

        # Guardar usuario relacionado al token
        try:
            user = User.get(User.id == data['id'])
            request.user = user
        except Exception as e:
            print("User error")
            print(e)

        return f(*args, **kwargs)

    return decorated
