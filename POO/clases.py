

import sys

sys.path.append('/home/henry/Escritorio/Backend/modulos')

from main import get_apiKey
from api_test import (
                            api_test,
                            api_login
                            )


class Auto2():

    def __init__(self, name):
        self.auto2 = 'tesla'
        self.name = name
        print('init clase Auto2', self.name)


class Auto3():

    def __init__(self, name):
        self.auto3 = 'tesla'
        self.name = name
        print('init clase Auto3', self.name)



class Auto(Auto2, Auto3):
    # algunas propiedas opcionales
    # modelo = 'tesla'
    color = 'rojo'
    motor = '1.5'
    ApiKeyGoogle = '129812'


    def __init__(self, kilometraje, numeroPuertas, year_auto, modelo):
        print('welcomen Auto!!!')
        self.kilometraje = kilometraje
        self.numeroPuertas = numeroPuertas
        self.year_auto = year_auto
        self.modelo = modelo

        print(self.kilometraje)
        print(self.numeroPuertas)
        print(self.year_auto)
        # super(Auto2, self).__init__(self)
        # super().__init__('autoTesla')
        Auto2.__init__(self, 'autoTesla')
        Auto3.__init__(self, 'autoNissan')

    def acelerar(self, velocidad):
        print('atribb',self.auto3)
        api_login('kminchelle', '0lelplR')


        print(f'INiciando auto {self.modelo}')
        print('acceder a propiedad desde los metodos',self.modelo, self.color, self.motor)
        if velocidad >= 100:
            print('acelerando auto')

        print(self.ApiKeyGoogle)
    

    def frenar(self, velocidad):
        if velocidad >= 50:
            print('frenenando auto')



auto_tesla = Auto('100km', '6 puertas', 1990, 'tesla')

print(auto_tesla.modelo)
print(auto_tesla.color)
print(auto_tesla.motor)

auto_tesla.motor = '2.5'
auto_tesla.color = 'verde'

print(auto_tesla.motor)

print(auto_tesla.color)


auto_tesla.acelerar(100)
# auto_tesla.frenar(50)

print('---------------------------------')

auto_nisan = Auto('50km', '2 puertas', 2023, 'nissan')
print(auto_nisan.modelo)
print(auto_nisan.color)
print(auto_nisan.motor)

print('---------------------------------')


auto_toyota = Auto('10km', '4 puertas', 2024, 'toyota')
print(auto_toyota.modelo)
print(auto_toyota.color)
print(auto_toyota.motor)