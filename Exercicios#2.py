def pares(lista):
    lista_pares = []
    
    for numeros in lista:
        if numeros % 2 == 0:
         lista_pares.append(numeros)
         
    
    return lista_pares    
         
     

lista_de_numeros = [4, 5, 6, 7, 8]

pares_lista = pares(lista_de_numeros)
print("Número de pares:", pares_lista)