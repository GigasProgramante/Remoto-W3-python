nums = []
inserir = True

while inserir:
    nota = input("Insira suas notas (deixe vazio para calcular a média): ")
    if nota == "":
        inserir = False
    else:
        nums.append(float(nota))

if len(nums) > 0:
    media = sum(nums) / len(nums)
    print(f"A média final é de: {media}")
else:
    print("Nenhuma nota foi inserida.")

# array.append(tipo_de_dado(variável)), adiciona o valor do variável ao final da array, esse é o jeito correto de adicionar dados a uma array vazia, de tamanho indefinido.