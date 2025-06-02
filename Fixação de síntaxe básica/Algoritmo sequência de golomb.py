# Função que calcula S(n) da sequência de Golomb
def golomb(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Fórmula recursiva
    result = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    memo[n] = result
    return result

# Chamada pra testar a função
num = int(input("Insira a posição da sequência que quer verificar: "))
print(golomb(num), "Na sequência de Golomb")