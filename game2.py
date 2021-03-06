import random

def hangman():
    list_word = ['cat', 'dog', 'fish', 'american']
    word = list_word[random.randint(0,3)]
    wrong = 0
    stages = ['',
              '________        ',
              '|               ',
              '|       |       ',
              '|       0       ',
              '|      /|\      ',
              '|      / \      ',
              '|               '
              ]
    rletters = list(word)
    board = ['__'] * len(word)
    win = False
    print('Welcom to licvidation!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Input a letter: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '__' not in board:
            print('You win! It was: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('You loose! It was: {}.'.format(word))

hangman()
