for i in range(1):
    print('I am programmer!')

name = 'MacLeod'
for character in name:
    print(character)

tv = ['Во все тяжкие',
      'Секретные материалы',
      'Фарго']
i = 0
for tv[i] in tv:
    tv[i] = tv[i].upper() 
    i += 1
''' Преобазование элементов списка
    в элементы из заглавных букв
'''
print(tv)

tv = ['Во все тяжкие',
      'Секретные материалы',
      'Фарго']
for i, peredachi in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
''' Преобазование элементов списка
    в элементы из заглавных букв
'''
print(tv)
