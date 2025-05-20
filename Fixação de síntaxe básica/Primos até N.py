'''Solicite um número N e imprima todos os números primos até esse valor.'''

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

import math

num = int(input("Escolha um número: "))

for i in range(num):
    if eh_primo(i):
        print(i)