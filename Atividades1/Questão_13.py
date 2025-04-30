"""13 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por
B e o valor de B por A e imprima na tela os valores."""

a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))

a, b = b, a

print(f"Após a troca, o valor de A é {a} e o valor de B é {b}.")