quant_dvd = 0
valor_aluguel = 0
faturamento_anual = 0

quant_dvd = input("Informe quantos DVD's a sua locadora possui: ")
quant_dvd = int(quant_dvd)

valor_aluguel = input("Informe o valor de aluguel por DVD: ")
valor_aluguel = int(valor_aluguel)

#1/3 dos dvds sao alugados no mes e faturamento anual
terco_dvd = quant_dvd / 3
dvd_por_mes = terco_dvd * valor_aluguel
faturamento_anual = dvd_por_mes * 12

#multa de 10% e valor ganho por mes                     # 1/3 dos DVDs são alugados
dvd_com_atraso = terco_dvd / 10                         # 1/10 dos alugados tem atraso
valor_multa_por_dvd = valor_aluguel * 0.10              # Multa é 10% do valor do aluguel
valor_multa_mes = dvd_com_atraso * valor_multa_por_dvd  # Valor total de multas

#2% dos dvds estraga e 1/10 é comprado para repor
dvd_estragados  = quant_dvd * 2 / 100 
repor_dvd = quant_dvd / 10
quant_final_dvd = quant_dvd - dvd_estragados + repor_dvd