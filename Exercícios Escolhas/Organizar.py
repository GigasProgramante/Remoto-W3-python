"""4 - Faça um programa que lê quatro valores: I, A, B e C, onde I é um número inteiro
e positivo e A, B, e C são quaisquer valores reais. O programa deve escrever os
valores lidos e:
• se I = 1, escrever os três valores A, B e C em ordem crescente;
• se I = 2, escrever os três valores A, B e C em ordem decrescente;
• se I = 3, escrever os três valores A, B, e C de forma que o maior valor fique
entre os outros dois;
• se I não for um dos três valores acima, dar uma mensagem indicando isto."""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
ind = int(input("Escolha a operação;\n1 para ordenar em ordem cresente;\n2 para oredenar em ordem decrescente;\n3 para colocar o maior no meio.\nEscolha: "))

nums = [num1, num2, num3]
nums.sort()

print (f"Os números digitados foram: {num1}, {num2}, {num3}")

match ind:
    case 1:
        print(f"Os números em ordem crescente são: {nums[0]}, {nums[1]}, {nums[2]}")
    case 2:
        print(f"Os números em ordem decrescente são: {nums[2]}, {nums[1]}, {nums[0]}")
    case 3:
        print(f"O maior número é: {nums[2]} e os outros dois são: {nums[0]}, {nums[1]}")
    case _:
        print("Número inválido! Escolha um número entre 1 e 3.")
