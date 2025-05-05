'''Calcular o fatorial de um número
Descrição: O programa pede um número e calcula seu fatorial.'''

num = (int(input("Insira o número que será fatorado: ")))
fat = num

while num > 1:
    i = num-1
    fat *= i
    num -= 1
print(fat)