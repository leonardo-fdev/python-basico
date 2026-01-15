"Exercício 1: Tipo de dados" 

string = "Tipo assim"
inteiro = 5
float = 5.0

"Extra"
boleano = True

print(type(string), type(inteiro), type(float), type(boleano))




"Exercício 2: Operadores"
while True:
 try:
  numero1 = int(input("Digite o primeiro número: "))
  numero2 = int(input("Digite o segundo número: "))
  break
 
 except:
    print("Digite um valor válido")

print(f"A adição desses números é:  {numero1 + numero2}")
print(f"A subtração desses números é:  {numero1 - numero2}")
print(f"A somultiplicação desses números é:  {numero1 * numero2}")
if numero2 != 0:
    print(f"A divisão desses números é {numero1 / numero2}")
    
else:
    print("Nenhum número pode ser divisivel por zero, tente novamente")
    
    
"Exercicio 3: Estrutura de controle"

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Você é maior de idade!")
    
else:
    print("Você é menor de idade!")
    




'''Exercício 4: Estrutura de dados'''
    
frutas = ["maça", "banana", "morango", "melão", "uva"]

print(frutas)
print(f"a primeira fruta é :  {frutas[0]}")
frutas.append("melancia")
print("Adicionado melancia", frutas)
fruta_removida = frutas.pop(1)
print("Removido banana", frutas)





"Exercicio 5: funçoes"

def salvacao(nome):
    return print(f"Olá, {nome}! Seja bem-vindo!")

nome = input("Digite o seu nome")
salvacao(nome)



    
    


    
    
