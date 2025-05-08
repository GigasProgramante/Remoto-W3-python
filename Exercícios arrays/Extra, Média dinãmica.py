nums = []  # Inicializa uma lista vazia
inserir = True

while inserir:
    nota = input("Insira suas notas (deixe vazio para calcular a média): ")
    if nota == "":  # Verifica se o input está vazio
        inserir = False
    else:
        nums.append(float(nota))  # Adiciona a nota convertida para float na lista

if len(nums) > 0:
    media = sum(nums) / len(nums)
    print(f"A média final é de: {media}")
else:
    print("Nenhuma nota foi inserida.")