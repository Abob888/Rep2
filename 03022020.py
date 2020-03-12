qs = ['Name? ',
      'Age? '
      ]
n = 0
while True:
    print('Press X')
    a = input(qs[n])
    if a == 'X':
        break
    n = (n + 1) % 2
    ''' Классный механизм циклического перебора цифр
работает с 2, 3 и 4'''
    
