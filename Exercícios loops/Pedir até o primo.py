'''Pedir números até o usuário digitar um número primo
Descrição: O programa pede números até o usuário digitar um número
primo.'''

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

while True:
    num = int(input("Insira o número, inserir um número primo encerra o programa: "))
    if is_prime(num):
        print(f"{num} é um número primo. Encerrando o programa.")
        break
    else:
        print(f"{num} não é um número primo. Tente novamente.")

#Usei IA, preciso refazer