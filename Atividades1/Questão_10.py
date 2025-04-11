"""
10 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a
média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi
aprovado ou reprovado. Para o aluno ser considerado aprovado sua média
final deve ser maior ou igual a 7."""

nome = str(input("Insira o nome do aluno: "))

num1 = float(input("Insira a primeira nota: "))
num2 = float(input("Insira a segunda nota: "))
num3 = float(input("Insira a terceira nota: "))
num4 = float(input("Insira a terceira nota: "))

media = (num1+num2+num3+num4)/4

if media < 7.0:
    print(nome, "está reprovado!!!")
else:
    print(nome, "está aprovado!!!")