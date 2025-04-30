#1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B e mostre se a soma é menor que C.

print("Digite o valor de A:")
a = int(input())
print("Digite o valor de B:")
b = int(input())
print("Digite o valor de C:")
c = int(input())

soma = int(a + b)

if soma == c:
    print("A soma de A e B é: ", soma, " igual que C")
elif soma < c:
    print("A soma de A e B é: ", soma, " e é menor que C")
else:
    print("A soma de A e B é:", soma, " e é maior que C")