from modulos.main import get_apiKey
from modulos.api_test import (
                            api_test,
                            api_login
                            )


# esto es un comentario
print('hola mundo, mi nombres es Henry!')

# definiendo las variables
usuario = 'erick'
edad = 19

print(usuario)
print(edad)

usuario = 'rosa'
edad = 33
print(usuario)
print(edad)


salidaApiKey =  get_apiKey()

print(salidaApiKey)


# api_test()


api_login('kminchelle', '0lelplR')