#Desafio foi fazer esse sistema sem o uso de ().

nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
soma = 0
media = 0

print("Programa para calcular média das notas.")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))
nota4 = int(input("Insira a quarta nota: "))

soma = nota1+nota2+nota3+nota4
media = soma/4

print("A média das notas é: ", media)