s = "string"
t = 5
a = 0
lista = list(s)
asci = [ord(x) for x in lista]
print(asci)

while a <= t-1:
    a += 1
    i = 0
    print(f"{asci}    CICLO: {a}")
    while i < len(asci):
        asci[i] += 1
        if asci[i] >= 123:
            asci.insert(i, 98)
            asci.insert(i, 97)
            asci.pop(i + 2)
        i += 1

solve = [chr(x) for x in asci]
solved = len(solve)

print(asci)
print(solve)
print(solved)