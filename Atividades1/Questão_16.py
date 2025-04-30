#16 - Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o
#quociente e o resto da divisão inteira entre eles.

a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))

quociente = a / b
resto = a % b

print (f"O quociente é {quociente} e o resto é {resto}.")