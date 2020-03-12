a = ['3', '5', '7']
i = 0
while True:
    print('Press X to escape or A to continue')
    b = input()
    if b == 'X':
        break
    else:
        c = input('Input a figure ')
        if c == a[i]:
            print('Bingo!')
        else:
            print('Tray again!')
        i = (i + 1) % 3
    
