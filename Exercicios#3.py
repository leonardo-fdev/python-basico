def erros(mensagems):
   
    while True:
      try:
        return(int(input(mensagems)))
      
      except ValueError:
        print("Digite um valor válido")
 
    

def numeros():
 
 lista_de_numeros = []
 
 
 while True:
     numero = erros("Digite um número: ")
     if numero == 0:
       break
 
     lista_de_numeros.append(numero)
 
  
 return lista_de_numeros



number = numeros()

def calculos_lista(calculo):
    soma_da_lista = sum(calculo) 
    print(f"A soma dos números digitados é: {soma_da_lista}")
    
    maior_numero = max(calculo) 
    print("O maior número digitado é: ", maior_numero)
    
    menor_numero = min(calculo)
    print("O menor número digitado é: ", menor_numero)
    
    media_numero = sum(calculo) / len(calculo)
    print("A média dos números digitados é: ", media_numero)

if number != [] :
 print(f"{len(number)} número(s) foram digitados: ", number)
 calculos_lista(number)
else:
    print("Nenhum número foi digitado")



    








  
  
    
      
 
        
 

