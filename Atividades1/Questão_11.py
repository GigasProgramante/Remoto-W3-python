"""
11 - Faça um algoritmo que leia o valor de um produto e determine o valor que
deve ser pago, conforme a escolha da forma de pagamento pelo comprador e
imprima na tela o valor final do produto a ser pago. Utilize os códigos da
tabela de condições de pagamento para efetuar o cálculo adequado.
Tabela de Código de Condições de Pagamento
1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
2 - À Vista no cartão de crédito, recebe 10% de desconto
3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
4 - Parcelado no cartão em três vezes ou mais, preço normal do produto
mais juros de 10%.
"""
valor_original = float(input("Insira o valor total da compra: "))
pagamento = int(input("Escolha a forma de pagamento:\n1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto;\n2 - À Vista no cartão de crédito, recebe 10% de desconto;\n3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros\n4 - Parcelado no cartão em três vezes ou mais, preço normal do produto.\nEscolha: "))

if pagamento == 1:
    valor_final = valor_original - (valor_original * 0.15)
    print("O valor final é de:", valor_final)
elif pagamento == 2:
    valor_final = valor_original - (valor_original * 0.10)
    print("O valor final é de:", valor_final)
elif pagamento == 3:
    valor_final = valor_original
    print("O valor final é de:", valor_final)
elif pagamento == 4:
    valor_final = valor_original + (valor_original * 0.10)
    print("O valor final é de:", valor_final)