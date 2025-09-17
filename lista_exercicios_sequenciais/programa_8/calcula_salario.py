por_hora = 0
horas_mes = 0
dias_mes = 0
salario = 0
por_dia = 0

print("Programa para calcular salário.")

por_hora = input("Digite o valor cobrado por hora: ")
por_hora = float(por_hora)
hora_mes = input("Digite o valor de horas trabalhadas por mês: ")
hora_mes = float(hora_mes)
dias_mes = input("Digite quantos dias do mês você trabalhou: ")
dias_mes = float(dias_mes)

salario = (por_hora * hora_mes) / dias_mes
por_dia = salario / dias_mes

print(f"O seu salário esse mes é: {salario:.2f}")
print(f"O valor médio por dia trabalhado é: R$ {por_dia:.2f}")
