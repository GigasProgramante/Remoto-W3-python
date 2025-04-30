#3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, 
# deverá somar os dois valores, caso contrário deverá multiplicar A por B. Ao final de qualquer 
# um dos cálculos deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela. 

print("Digite o valor de A: ")
a = (int(input()))
print("Digite o valor de B: ")
b = (int(input()))

if a == b:
    c = a + b
    print("A soma de A e B é: ", c)
else:
    c = a * b
    print("A multiplicação de A e B é : ", c)