nome = input("Digite seu nome: ")

print(f"Olá {nome}!!!")

min = int(input("Digite quantos minutos foram falados no mês: "))

if min < 200 and min >= 0:
    conta = min * 0.20
else:
    if min <= 400 and min >= 0:
        conta = min * 0.18
    if min > 400 and min >= 0:
        conta = min * 0.15



if conta < 0:
    print("Valor invalido!")
else: 
    print(f"O total de conta é R${conta:.2f}!")


