'''Exibir os múltiplos de 3 entre 1 e 30
Descrição: O programa deve imprimir todos os números múltiplos de 3 entre
1 e 30.'''

num = 0

while num <= 30: 
    num += 1
    if num % 3 == 0:
        print(f"{num}\n")
