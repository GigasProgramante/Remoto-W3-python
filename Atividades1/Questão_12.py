"""12 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela
o nome da pessoa e se ela é maior ou menor de idade."""

nome = str(input("Insira o nome: "))
idade = int(input("Insira sua idade: "))

if idade < 18:
    print(nome, "é menor de idade!")
else:
    print(nome, "é maior de idade!")