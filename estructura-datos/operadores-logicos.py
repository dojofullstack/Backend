


# operadores logicos
"""
 3 operadores
 or (al menos una debe en evaluar en true para retornar true)

false or true = true
true or false = true
true or true = true
false or false = false


 and
 (ambos deben en evaluar true para retornar true)
true and true = true
las demas false



 negacion (not)

"""


# practicando operador logico or
isAdmin = False
nombre = 'pedro'

salida =  isAdmin or len(nombre) > 10
# print(salida)


# practicando operador logico and
isAdmin = True
salida2 =  isAdmin and len(nombre) > 3
salida3 =  isAdmin and nombre == 'pedro'
salida4 =  isAdmin and nombre != 'erick'

# print(salida4)


# operador de negacion 'not'

isUserVip = True
email = ''
userAge = 0
profile = {}
series = []


print(not series)
print(not profile)
print(not email)
print(not userAge)
# print(not isUserVip)