"""14 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima
na tela quantos anos, meses e dias essa pessoa já viveu. Leve em
consideração o ano com 365 dias e o mês com 30 dias."""

ano_n = int(input("Insira o ano em que você nasceu: "))
mes_n = int(input("Insira o mes de nascimento: "))
dia_n = int(input("Insira o dia de nascimento: "))

ano = int(input("Insira o ano atual: "))
mes = int(input("Insira o mes atual: "))
dia = int(input("Insira o dia atual: "))

ano_total = ano - ano_n
mes_total = mes - mes_n
dia_total = dia - dia_n

if dia_total <= 0:
    dia_total += 30
    mes_total -= 1

if mes_total <= 0:
    mes_total += 12
    ano_total -= 1

print(ano_total, ":", mes_total, ":", dia_total)