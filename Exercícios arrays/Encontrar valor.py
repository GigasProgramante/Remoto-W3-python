"""04 - Implemente um algoritmo que leia 5 valores inteiros e os armazene em um
vetor. Em seguida, o algoritmo deve solicitar que o usuário informe um número para
busca. O programa deve verificar se esse número está presente no vetor e exibir
uma mensagem indicando se o valor foi encontrado ou não."""

nums = [0] * 5
está = False

for i in range(5):
    nums [i] = int(input(f"Insira o valor da possição {i}: "))

valor = int(input("Insira o valor que queres verificar a presença na array: "))

for i in range(5):
    if nums[i] == valor:
        está = True

if está:
    print("O número está presente na array!")
else:
    print("O número não está no grupo!")