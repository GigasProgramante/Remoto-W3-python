"""03 - Faça um algoritmo que leia 4 notas reais de um aluno, armazenando-as em um
vetor. Depois, calcule e exiba a média aritmética das notas."""

nums = [0] * 4
soma = 0

for i in range(4):
    nums [i] = int(input(f"Insira o valor da possição {i}: "))

for i in range(4):
    soma += nums[i]

media = soma/4

print("A media final é de: ", media)
