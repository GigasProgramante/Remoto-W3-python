'''Peça ao usuário um número entre 1 e 10. Continue pedindo até ele digitar corretamente (use while).'''
digitado = -1
while digitado < 0 or digitado > 10 or digitado == "_":
    digitado = int(input("Insira o número a verificar (1-10): "))
    if digitado < 0 or digitado >10 or digitado == "_":
        print("Numero incorreto!!!")
else:
    print("Número válido, programa encerrado!!!")