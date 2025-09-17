val_metro = 0
val_centimetro = 0

print("Programa para converter metros em centpimetros.")

val_metro = input("Insira o valor em metros: ")
val_metro = int(val_metro)

val_centimetro = val_metro * 100

print(f"O valor {val_metro} em centimetros é {val_centimetro:.2f}")