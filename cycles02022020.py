tv = ["Highlander", "Limitless",
      "New Hope"]
mov = ['Transformers', 'Star Wars',
       'Enterprise']
all_m = []

for show in tv:
    show = show.upper()
    print(show)
    all_m.append(show)

for show in mov:
    show = show.upper()
    print(show)
    all_m.append(show)
''' Программа объединяет два списка в 1
    и выводит его
'''
print(all_m)
