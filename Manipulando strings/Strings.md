Strings funcionam como arrays em python

Por conta disso, os caracteres de uma string pode ser acessados da mesma maneira como podemos acessar elementos de uma array

a = "Hello, World!"
print(a[1])

por ser uma array, também podemos acessar os elementos atravé de loops

for x in "banana":
  print(x)

podemos usar a função len(), para retornar a quantidade de caracteres em uma array

a = "Hello, World!"
print(len(a))

Podemos checar se um elemento está presente em uma array usando a palavra chave in

txt = "The best things in life are free!"
print("free" in txt)

E também podemos usálo como conector lógico em if, por exemplo:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")