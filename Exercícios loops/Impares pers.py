'''Exibir os números ímpares entre dois valores digitados pelo
usuário
Descrição: O usuário digita dois números e o programa exibe todos os
números ímpares entre eles.'''

ini = (int(input("Escolha o primeiro número do grupo: ")))
fim = (int(input("Escolha o último número do grupo: ")))

i = ini

while i >= ini and i <= fim - 1:
    i += 1
    if i % 2 != 0:
        print(i)
    else:
        continue