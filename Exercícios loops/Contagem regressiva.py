'''Exibir uma contagem regressiva personalizada
Descrição: O usuário digita um número N e o programa exibe uma
contagem regressiva até 0.'''

contagem = (int(input("Escolha o número do qual será iniciado a contagem: ")))

while contagem > 0:
    contagem -= 1
    print(contagem)