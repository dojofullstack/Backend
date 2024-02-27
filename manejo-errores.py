

"""
    para controlar errrores
    en tiempo de ejec.
"""


try:
    edad = input('ingresa tu edad?')
    print('hola mundo')
    print(edad + 20)
except Exception as error :
    print(error)
    print('capturadno error, solucionando...')
    edad = int(edad)
    print(edad + 20)




print('final del programa, completado correctamente')