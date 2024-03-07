

# funcion en un conjunto de intrucciones en espera de ser llamado o ejecutado.

def run(miembro, creditos):
    print('acelerar')
    # miembro = 'FREE'

    if miembro == 'VIP':
        print('tienes acceso!')
        return 'usuario VIP'
    
    for i in range(creditos):
        print(i)
    
    return 'usuario FREE'



saida_funcion =  run('FREE', 3)
print(saida_funcion)