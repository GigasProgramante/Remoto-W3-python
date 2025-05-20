'''Peça ao usuário um valor inicial, final e o passo. Faça um for que imprima essa contagem.'''
inicial = int(input("Insira o valor inicial: "))
final = int(input("Insira o valor final: "))
passo = int(input("Insira o valor de cada passo: "))
soma = inicial + passo

for i in range(inicial, final, passo):
    print(i)