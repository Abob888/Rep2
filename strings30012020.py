print('I jumped in my car. It was funny')
print('I jumped in my car. It was funny'.split('.')) #Разделение строки на 2

words = ['one',
         'two',
         'three',
         'four',
         'five']
one = ' '.join(words)
'''
      Объединение элементов списка в строку
      со вставленным пробелом.
'''
print(one)

s = '    London   jazz    '
s = s.strip() # Удаление пробелов в начале и конце строки
print(s)

equ = 'All people are the same'
equ = equ.replace('are', '#')
''' Замена слова или символа
    другим символом или словом'''
print(equ)

print('people'.index('o')) # Номер первого вхождения искомого символа

try:
    'I jumped in my car. It was funny'.index('x')
except:
    print('"X" is not defined') # Обработка отсутствия вхождения

print('string1\nspring2\nstring3\nstring4') # Симол \n переносит на след. строку

tex = '''Встроенный буффер 60Мб позволяет компенсировать кратковременные потери
связи, а при установке micro SD/SDHC/SDXC возможно применение технологиии'''

print(tex[0:15]) # Первый фрагмент текста
print(tex[20:45]) # Второй фрагмент текста
print(tex[:55]) # Ноль можно не печатать
print(tex[56:]) # До конца строки тоже можно не печатать
  


