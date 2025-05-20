nums = [2,0,2,1,1,0,0,0,0,1,1,1,2,2,2,0]
tamanho = len(nums)
zeros = nums.count(0)
ums = nums.count(1)
dos = nums.count(2)
fim = zeros+ums+dos
nums = nums.clear()
for i in range(tamanho):
    nums.append(0)
for i in range(tamanho):
    nums.append(1)
for i in range(tamanho):
    nums.append(2)
print(nums)

## incompleto