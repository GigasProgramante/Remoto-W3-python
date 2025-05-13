digits = [9,9]

ultimo = digits[-1]
ultimo += 1
digits[-1] = ultimo

for i in range(len(digits)-1, -1, -1):
    if digits[i] == 10:
        digits[i] -= 10
        digits[i-1] += 1
        digits[-1]=0
    if digits[0] == 0:
        digits.insert(0, 1)
print(digits)