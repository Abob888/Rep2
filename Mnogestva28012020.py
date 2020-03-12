a = {i ** 2 for i in range(10)}
print(a)

words = ['hello', 'daddy', 'hello', 'mum']
print(set(words))

aut = "Smith"
print(aut[0])
print(aut[1])
print(aut[2])
print(aut[3])
print(aut[4])

print(aut[-5])

print('Andre {}'.format('Agassi'))
last = 'Sampras'
print('Pit {}'.format(last))

player = 'Andre Agassi'
number_one = '1999'

print('{} van the US Open in {}.'.format(player, number_one))

n1 = input('person: ')
n2 = input('verb: ')
n3 = input('subject')
n4 = input('name')

r = '''As usual, {} {} {} {}
    '''.format(n1,
               n2,
               n3,
               n4)
print(r)
