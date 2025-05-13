"""01 - Desenvolva um algoritmo que leia 5 números inteiros e os armazene em um
vetor. Após a leitura, o programa deve exibir todos os valores digitados pelo usuário,
um em cada linha."""

nums = [0] * 5

for i in range(5):
    nums [i] = input(f"Insira o valor da possição {i}: ")

for i in range(5):
    print(nums[i],)