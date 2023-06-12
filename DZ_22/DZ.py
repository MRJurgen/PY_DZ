quantity_1=int(input('Количество элементов в 1 множестве : '))
quantity_2=int(input('Количество элементов в 2 множестве : '))

first_list = []
second_list = []

print("Задайте элементы первого множества")
for i in range(quantity_1):
    first_list.append(int(input(f"n [{i}] = ")))

print("Задайте элементы второго множества")
for i in range(quantity_2):
    second_list.append(int(input(f"n [{i}] = ")))

my_list = []

for i in range(quantity_1):
    for j in range(quantity_2):
        if(first_list[i]==second_list[j]):
            my_list.append(first_list[i])

my_list.sort

print(set(my_list))
print(first_list)
print(second_list)
