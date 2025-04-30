# 7 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente. 

print("Digite o valor de A: ")
a = int(input())
print("Digite o valor de B: ")
b = int(input())
print("Digite o valor de C: ")
c = int(input())

if a > b and a > c:
    maior = a
    if b > c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b
elif b > a and b > c:
    maior = b
    if a > c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a
else:
    maior = c
    if a > b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a
print("Valores em ordem decrescente:", maior, meio, menor)