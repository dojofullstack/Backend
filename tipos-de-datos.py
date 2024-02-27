


# Tipo de dato string

'''
    Tabajando con 
    el Tipo de dato
    string
'''

email = 'erick@gmail.com'
nombre = 'manuel sanchez'

# print(type(email))
# print(type(nombre))



# print( dir(email) )

# print( nombre.capitalize() )
# print( nombre.title() )
# print( nombre.count('manuel') )

# print( nombre.startswith('sanchez') )
# print( nombre.endswith('chez') )


# print( email.replace('gmail', 'hotamil') )

comentario = '\n  informees \t sobre el bootcamp    \n \t'

# print( comentario.strip('\n').strip(' ').strip('\t') )
# print(comentario)
# strip
# find
# split

# print( nombre.find('xxyz') )


# frase = 'simple es mejor que complejo'
# frase_en_listas =  frase.split(' ')

# # print(frase_en_listas)
# print('@'.join(frase_en_listas))



# la funciones que indican el tipo de dato, se utilizan para conversion
# print( str(True))




'''
    Tabajando con 
    el Tipo de dato
    numeral
'''


edad = 123
precio = 9.534

# suma
# sumando = edad + 10
# edad = edad + 10
# edad += 10
# edad -= 10
# edad *= 10
# edad /= 10
# edad **= 10
# print(edad)
# edad += 1

# print( type(edad) )
# print( type(precio) )

# print(type(int('123')))
# print(type(float('3.5')))




'''
    Tabajando con 
    el Tipo de dato
    Boleano
'''


isAdmin =  True
isPremim = False
# print(isAdmin)
# print(type(isAdmin))

# print(isPremim + isPremim)



'''
    Tabajando con 
    el Tipo de dato
    Listas
'''


frutas = ['naranajs', 'uvas', 'peras', 'uvas']
frutasAcidas = ['pina', 'toronja']

# print(frutas)

# print(type(frutas))

# print(dir(frutas))

frutas.append('mandarinas')

# frutas.clear()

# print(frutas.count('uvas'))

frutasAcidas.extend(frutas)

# print(frutasAcidas)



# print(len(nombre))
# print(len(frutasAcidas))

# print(frutasAcidas[0])
# print(frutasAcidas[1])

# frutasAcidas.remove('toronja')
# print(frutasAcidas)

# frutasAcidas.sort()
# print(frutasAcidas)



'''
    Tabajando con 
    el Tipo de dato
    Diccionario
'''

miembro = {
    'plan': 'PREMUM',
    'time': '30 days'
}

perfil = {
    'email': 'pedro@gmail.com',
    'edad': 12,
    'siEsAdmin': True,
    'permisos': ['escribir', 'leer', 'team'],
    'config': {
        'color': 'rojo',
        'identificador': 1231
    }
}

# print(perfil)
# print(type(perfil))
# print(dir(perfil))

# print( perfil['emailVerif'] )

# print( perfil.get('emailVerif', 'admin@dojo.com'))

# print('final del programa, termino correctamente :)')

# print(perfil.keys())
# print(perfil.values())

# print(perfil.items())

# para crear nuevas keys
perfil['password'] = 1212121

# para actualizar
perfil['edad'] = 33

# para actualizar

# del perfil['passwordNew']
# perfil.pop('passwordNew')


# perfil.update(miembro)


# print(perfil)



'''
    Tabajando con 
    el Tipo de dato
    Tuplas
'''


ApiKey = ('ApiKeyGoogle1029819281', '01920910')

print(ApiKey)
print(type(ApiKey))

# ['count', 'index']

print(len(ApiKey))

print(ApiKey.count('ApiKeyGoogle1029819281'))
print(ApiKey.index('ApiKeyGoogle1029819281'))

# print(dir(ApiKey))