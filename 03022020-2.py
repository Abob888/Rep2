for i in range(1, 6):
    if i == 3:
        continue # вариант пропуска итерации
    print(i)

a = 1
while a <= 5:
    if a == 3:
        a += 1
        continue # вариант пропуска итерации
    print(a)
    a += 1

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)


while input('y or n? ') != 'n':
    for c in range(1, 6):
        print(c)
