"""3 - Construa um algoritmo que leia um número inteiro de 1 a 7 e informe o dia da
semana correspondente, sendo domingo o dia de número 1. Se o número não
corresponder a um dia da semana, mostre uma mensagem de erro."""

dia = int(input("Digite um número correspondenete a um dia da semana (1-7): "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido! Digite um número entre 1 e 7.")

