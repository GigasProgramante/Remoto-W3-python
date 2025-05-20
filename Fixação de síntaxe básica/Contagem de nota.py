'''Solicite um valor de saque e informe quantas notas de 100, 50, 20, 10 e 5 seriam entregues.'''

saque = int(input("Insira a quantidade que será sacada (Múltiplo de cinco): "))
origem = saque
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0

while saque >= 100:
    saque -= 100
    cem += 1
while saque >= 50:
    saque -= 50
    cinquenta += 1
while saque >= 20:
    saque -= 20
    vinte += 1
while saque >= 10:
    saque -= 10
    dez += 1
while saque >= 5:
    saque -= 5
    cinco += 1
print(F"Saque no valor de {origem}, com as sequintes cédulas:\n100: {cem}\n50: {cinquenta}\n20: {vinte}\n10: {dez}\n5: {cinco}")