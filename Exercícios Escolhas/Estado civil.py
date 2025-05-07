"""Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e
mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo,
Divorciado, Desquitado). Mostre uma mensagem de erro, se necessário."""

estado = str(input("Digite a primeira letra do seu estado civivl: "))

estado = estado.lower()

match estado:
    case 's':
        print("Solteiro(a)")
    case 'c':
        print("Casado(a)")
    case 'v':
        print("Viúvo(a)")
    case 'd':
        print("Divorciado(a)")
    case 'q':
        print("Desquitado(a)")
    case _:
        print("Estado civil inválido!")

