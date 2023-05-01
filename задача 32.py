# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint
a = int(input('введите количество элементов в массиве:'))
list = []
for i in range(a):
    list.append(randint(0,a))
print(list)
max_n = int(input())
min_n = int(input())
list_2 = 0

for i in range(len(list)):
    if min_n <= i <= max_n:
        
        print(list_2.index(i))
