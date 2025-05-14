x = 121
is_palindrome = False

digitos = str(x)

for i in range(len(digitos)):
    if digitos[i] == digitos[-i-1]:
        is_palindrome = True
    elif digitos[i] != digitos[-i-1]:
        is_palindrome = False
        break 

print(is_palindrome)