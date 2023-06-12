quantity=int(input('Количество элементов в массиве : '))
value_to_find=int(input('Какое число искать : '))

there_is = 0
my_list = []

for i in range(quantity):
    my_list.insert(i,i+1)
    if (my_list[i]==value_to_find):
        there_is+=1

print(my)
print(there_is)



