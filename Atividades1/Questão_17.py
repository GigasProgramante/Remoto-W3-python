#17 - Faça um algoritmo que efetue o cálculo do salário líquido de um
#professor. As informações fornecidas serão: valor da hora aula, número de
#aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela
#o salário líquido final.

horas = int(input("Insira o número de aulas lecionadas: "))
valor = float(input("Insira o valor da hora aula: "))
inss = int(input("Insira a porcentagem do inss:"))

total = horas * valor

perc = inss/100

final = total - (perc * total)

print(f"O salário final é de :{final}")