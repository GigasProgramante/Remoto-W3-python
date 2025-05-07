'''1 - Crie um algoritmo chamado Estacoes. Este algoritmo deve ler uma data e
armazenar na variável mes um número entre 1 e 12, correspondendo a um dos
meses do ano. No final, você deve imprimir uma mensagem conforme o exemplo:
"A estação do ano correspondente ao mês 3 é Verão"
Considere a estação prevalente para cada mês:
a) Janeiro (1): Verão
b) Fevereiro (2): Verão
c) Março (3): Verão
d) Abril (4): Outono
e) Maio (5): Outono
f) Junho (6): Outono
g) Julho (7): Inverno
h) Agosto (8): Inverno
i) Setembro (9): Inverno
j) Outubro (10): Primavera
k) Novembro (10): Primavera
l) Dezembro (10): Primavera'''

mes = (int(input("Escolha um número relativo a um mês do ano: ")))

match mes:
    case 1 | 2 | 3:
        estacao = "Verão"
    case 4 | 5 | 6:
        estacao = "Outono"
    case 7 | 8 | 9:
        estacao = "Inverno"
    case 10 | 11 | 12:
        estacao = "Primavera"
    case _:
        estacao = "Inválido"

if estacao == "Inválido":
    print("Número inválido")
else:
    print(f"A estação do ano de número {mes} é a {estacao}")