"""Archivo para manejar funciones genericas via Ajax"""
import json
import requests
from api.settings_secret import API_URL


class Api(object):
    """Conector Web API"""
    _url = API_URL

    def get(self, token, slug='', arg=None, data=None):

        if token:
            headers = {'token': token}
        else:
            headers = None

        try:

            result = requests.get(
                self._url + slug, headers=headers, params=arg, data=data)
            return result

        except Exception as e:
            print(e.args)
            print("---------------ERROR GET---------------")
            return None

    def post(self, token='', slug='', arg=None):

        if token:
            headers = {'token': token}
        else:
            headers = None

        try:
            result = requests.post(self._url + slug, headers=headers, json=arg)
            return result

        except Exception as e:
            print(e.args)
            print("---------------ERROR POST---------------")
            return None


def ajax_service(request):
    """Funcion generica para reenviar peticiones"""
    data = json.loads(request.body.read().decode('utf-8'))  # Extraigo datos
    obj_api = Api()
    method = request.method

    if 'url' in data:  # url es obligatorio
        url = data['url']
    else:
        return json.dumps({})

    if 'use_method' in data:
        method = data['use_method']

    if 'token' in data:
        token = data['token']
    else:
        token = None

    # Ejecutamos el metodo correspondiente en Api Class
    resp = getattr(obj_api, method.lower())(slug=url, token=token, arg=data)
    data = resp.json()

    try:
        # Retornamos el status_code de la API
        data['status_code'] = resp.status_code
    except TypeError as e:
        print(e)

    return json.dumps(data)
