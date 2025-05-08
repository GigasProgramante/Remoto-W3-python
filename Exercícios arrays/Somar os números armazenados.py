"""02 - Crie um algoritmo que leia 5 números inteiros, armazene-os em um vetor e
calcule a soma de todos os elementos. Ao final, exiba o resultado da soma."""

nums = [0] * 5
soma = 0

for i in range(5):
    nums [i] = int(input(f"Insira o valor da possição {i}: "))

for i in range(5):
    soma += nums[i]

print(soma)