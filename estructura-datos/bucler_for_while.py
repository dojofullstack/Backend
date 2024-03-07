


""" iteradores for y while """


series = ['viginkos', 'theBingbang', 'spiderman', 'superman']


# for item in series:
#     print(item)


# con el indice de cada elemento
# for (index, item) in enumerate(series):
#     # print(item[0], item[1])
#     print(index, item)



# print( list(range(1000)) )


# for key in range(5,10):
#     print(key)




series2 = []

# for item in series:
#     if item == 'viginkos' and len(item) > 3:
#         print('si existe viginkos')
#         # break
#         continue

#     print(item)

#     for key in series2:
#         print(key)




"""
    bucle while 
    iteramos de forma indefenidia sobre algun evento estado
"""

monitorActive = True
contador = 0

while monitorActive:
    contador += 1
    desea_conitnuar = input('desea continuar???')

    if desea_conitnuar == 'no':
        print('finzaliando while')
        monitorActive = False
        # break

    print('ejeutando codigo', contador)

