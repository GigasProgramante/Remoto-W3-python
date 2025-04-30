# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor. 

print("Escolha um número: ")
num = int(input())

antecessor = num - 1
sucessor = num + 1

print(antecessor, " < ", num, " > ", sucessor)