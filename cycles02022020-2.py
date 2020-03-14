for i in range(0, 10):
    print(i + 1)

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1

print('Happy new year!')

for i in range(0, 100):
    print(i)
    if i >= 50:
        break

qs = ['What is your name? ',
      'How old are you? ',
      'What are you doing? ']

n = 0
while True:
    print('Input X for escape.')
    a = input(qs[n])
    if a == 'X':
        break
    n = (n + 1) % 3
