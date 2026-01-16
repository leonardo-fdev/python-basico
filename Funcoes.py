'''
def soma():
    
    numero1 = int(input("Digite o primeiro número para somar: "))
    numero2 = int(input("Digite o segundo número para somar: "))
    
    resultado = numero1 + numero2
    return resultado


resultado = soma() 
print(f"O resultado da soma é : {resultado}")



def saldacao():
    nome = input("Digite o seu nome : ")
    return nome


nome = saldacao()
print( f"Olá {nome}! Seja bem-vindo(a).")

'''


def dobro(n1):
    return n1 * 2

numero = (int(input("Digite um número para ser dobrado!  ")))

resultado = dobro(numero)
print (resultado) 
    
