GASOLINA = 4.97
ALCOOL = 5.78
valor = 0.0

nome = input("Digite seu nome: ")

print(f"Olá {nome}!!!")

combustivel = input("Digite G - Gasolina e A - Alcool: ")
letra = combustivel.upper()
quantidade = float(input("Digite a quantidade de litros: "))

if letra == "G" and quantidade > 0:
    valor = quantidade * GASOLINA
   
if letra == "A" and quantidade > 0:
    valor = quantidade * ALCOOL

if (letra == "G" or letra == "A") and quantidade > 0:
    print(f"Valor total: {valor:.2f}.")
else:
    print("Valores invalidos.")
