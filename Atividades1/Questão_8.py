# 8 - Desenvolva um algoritmo que calcule o IMC (Índice de Massa Corporal) de
# uma pessoa. O programa deve:
# A. Pedir o sexo do usuário (M para masculino e F para feminino).
# B. Solicitar o peso (em kg) e a altura (em metros).
# C. Calcular o IMC utilizando a fórmula: IMC = peso / (altura) 2
# Tabela Condições IMC:
#Abaixo de 18,5 | Abaixo do peso

#UNIVERSIDADE DO CONTESTADO – UNC

#CANOINHAS – CONCÓRDIA – CURITIBANOS - MAFRA - PORTO UNIÃO – RIO NEGRINHO
#Correio eletrônico: reitoria@unc.br / Home Page: www.unc.br

#Av. Pres. Nereu Ramos, 1071 – Caixa Postal, 111 PABX/FAX: (047) 3641-5500 - CEP: 89.306-076 - Mafra – SC
#Mantida pela FUNDAÇÃO UNIVERSIDADE DO CONTESTADO - FUNC - CNPJ: 83.395.921/0001-28

#Desenvolvimento de Software I
#Leandro Bona
#Peso 40%

#Entre 18,6 e 24,9 | Peso ideal (parabéns)
#Entre 25,0 e 29,9 | Levemente acima do peso
#ntre 30,0 e 34,9 | Obesidade grau I
#Entre 35,0 e 39,9 | Obesidade grau II (severa)
#Maior ou igual a 40 | Obesidade grau III (mórbida)
#D. Exibir o IMC calculado e a condição correspondente.
#E. Garantir que o usuário digite um sexo válido (M ou F).

sexo = ""

while sexo not in ["F", "f", "M", "m"]:
    sexo = input(str("Escolha o sexo, M para masculino, F para feminino: "))

print("Insira seu peso: ")
peso = float(input())

print("Insira sua altura: ")
altura = float(input())

IMC = peso / (altura*2)

if IMC <= 18.6 :
    print("Abaixo do peso ideal! \nIMC: ", IMC)
elif IMC >= 18.6 and IMC <= 24.9:
    print("Peso ideal (parabéns) \nIMC: ", IMC)
elif IMC >= 25.0 and IMC <= 29.9:
    print("levemente acima do peso \nIMC: ", IMC)
elif IMC >= 30.0 and IMC <= 34.9:
    print("Obesidade grau I. \nIMC: ", IMC)
elif IMC >= 35.0 and IMC <= 39.9:
    print("Obesidade grau II (severa) \nIMC: ", IMC)
elif IMC > 40:
    print("Obesidade grau III (mórbida) \nIMC: ", IMC)