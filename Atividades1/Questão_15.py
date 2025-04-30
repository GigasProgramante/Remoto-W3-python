"""15 - Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem
1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e
imprima na tela em quantos anos serão necessários para que Francisco seja
maior que Sara."""

francisco = 150  # altura em cm
sara = 110  # altura em cm
anos = 0
while francisco >= sara:
    francisco += 2
    sara += 3
    anos += 1
print(f"Francisco será maior que Sara em {anos} anos.")