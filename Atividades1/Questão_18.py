#18 - João Papo-de-Pescador, homem de bem, comprou um microcomputador
#para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um
#peso de peixes maior que o estabelecido pelo regulamento de pesca do
#estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
#excedente. João precisa que você faça algoritmo que leia a variável P (peso
#de peixes) e verifique se há excesso. Se houver, gravar na variável E
#(Excesso) e na variável M o valor da multa que João deverá pagar. Caso
#contrário mostrar tais variáveis com o conteúdo ZERO

peso = int(input("Insira o peso pescado: "))

if peso <= 50:
    excesso = 0
    multa = 0

    print("Excesso: ", excesso, "\nMulta: ", multa)
else:
    excesso = peso - 50
    multa = excesso * 4.00
    print("Excesso: ", excesso, "\nMulta: ", multa)