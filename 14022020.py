rock = []
country = []

def collect_songs():
    song = 'Song name: '
    ask = 'Input r (rock) or c (country). Input X to go away.'

    while True:
        genre = input(ask)
        if genre == 'X':
            break

        if genre == 'r':
            rk = input(song)
            rock.append(rk)

        elif genre == 'c':
            cy = input(song)
            country.append(cy)

        else:
            print('False!')
        print(rock)
        print(country)

collect_songs()
