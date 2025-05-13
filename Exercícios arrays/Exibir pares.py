"""05 - Desenvolva um algoritmo que leia 6 números inteiros e os armazene em um
vetor. Após a leitura, o programa deve percorrer o vetor e exibir apenas os valores
pares que foram digitados."""

nums = [0] * 6


for i in range(6):
    nums [i] = int(input(f"Insira o valor da possição {i}: "))

for i in range(6):
    if nums[i] % 2 == 0:
        print(nums[i])