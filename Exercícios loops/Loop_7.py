'''Validar uma nota entre 0 e 10
Descrição: O programa pede uma nota ao usuário até que ele digite
um valor válido entre 0 e 10.'''

nota = -1

while nota < 0 or nota > 10:
    print('Nota inválida!')
    nota = (int(input('Digite uma nota entre 0 e 10: ')))
    if nota >= 0 and nota <= 10:
        break
print(f'Nota válida: {nota}')