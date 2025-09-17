val_real = 0
cotacao_dolar = 0
cotacao_euro = 0
val_dolar = 0
val_euro = 0

print("Programa para converter reais em Dolar e Euro")
val_real = input("Insira o valor em real a ser convertido: ")
val_real = int(val_real)
cotacao_dolar = input("Cotação do Dolar: ")
cotacao_dolar = float(cotacao_dolar)
cotacao_euro = input("Cotação do Euro: ")
cotacao_euro = float(cotacao_euro)

val_dolar = val_real/cotacao_dolar
val_euro = val_real/cotacao_euro


print(f"Resultado da conversão: Em Dolar: {val_dolar:.2f}  e em Euro: {val_euro:.2f}")