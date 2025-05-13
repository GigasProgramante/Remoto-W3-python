s = "hello"
valores = []

array_de_digitos = [x for x in s]

asci = [ord(x) for x in array_de_digitos]

for i in range(len(asci) - 1):
    num1 = asci[i]
    num2 = asci[i+1]
    diff = num1 - num2
    diff_abs = abs(diff)
    valores.append(diff_abs)

soma = sum(valores)
print(soma)