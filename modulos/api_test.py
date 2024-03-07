import requests



def api_test():
    print('testing apis')

    respuesta = requests.get('https://dummyjson.com/products')

    data = respuesta.json()

    for producto in  data.get('products'):
        print(producto)
        print('\n')




def api_login(usuario, password):
    print('testing apis')

    credenciales = {
    'username': usuario,
    'password': password,
    }

    respuesta = requests.post('https://dummyjson.com/auth/login', data=credenciales)

    data = respuesta.json()
    print(data)
    return data
