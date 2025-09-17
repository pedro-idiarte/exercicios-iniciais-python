val_celsius = 0
val_farenheight = 0

print("Programa para converter celsius para farenheight")

val_celsius = input("Insira o valor em celsius: ")
val_celsius = int(val_celsius)
val_farenheight = 1.8 * val_celsius + 32

print("O resultado da conversão é: ",val_farenheight)