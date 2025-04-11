# Em python, não existe um comando especifico para definir uma variavel, invés disso, podemos simplesmente atribuir um valor a uma variavel.
x = 10
palavra = "Olá Mundo!"
# O python é uma linguagem de tipagem dinâmica, ou seja, não precisamos declarar o tipo da variavel, o python infere o tipo da variavel automaticamente.
#Os tipos de variaveis são os mesmos das outra lnguagems, a tipo é definido automaticamente dependendo da forma que a variavel é atribuida.

# Para especificar o tipo de variavel, podemos usar algo chamado casting.
y = str(x) # Faz com que a variavel seja obrigatoriamente do tipo string.

#Podemos expressar o tipo de uma variavel usando
print(type(x))

#Duas variáveis, tipo "a" e "A", não se sobrepõem, e são duas variáveis completamente diferentes

#Da pra definir diversas variáveis em uma única linha.
x, y, z = 1, 2, 3

#Da pra definir diversas variáveis com um mesmo valor
x = y = z = "Laranja"

#Da pra definir diversos valores a uma única variável, criando uma coleção, que pode ser desmostada depois
var = [1, 2, 3]

#Desmontando
x, y, z = var

#Print de diversos valores pode usar "," ou "+", em texto "," exibe com um espaço, enquanto "+" exibe sem espaço, porém usar "+" não funciona com diferentes tipos de variavies, e "+" com variáveis numéricas faz a operação de soma
