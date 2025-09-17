diametro = 0
raio = 0
area = 0
dobro_area = 0

print("Programa para calcular o dobro da área.")

diametro = input("Insira o diametro: ")
diametro = int(diametro)

raio = diametro/2
area = 3.14 * (raio * raio)
dobro_area = area * 2

print(f"O dobro de {area:.2f}cm2 é {dobro_area:.2f}cm²")