locations = [] # Составляем список из кортежей

tula = (54, 36)
moscow = (55, 37)

locations.append(tula)
locations.append(moscow)

print(locations)


bday = {"me":
        "11.04.1983",
        "Ann":
        "11.04.1990"}

ml = [bday] # Делаем словарь списком
print(ml)
spisok = (bday,) # Делаем словарь кортежем
print(spisok)

ru = {"Place":
      (55, 37),
      
      "People":
      ["Ivanov", "Petrov", "Sidorov"],

      "Facts":
      {"sity": "Moscow",
       "country": "Russia"}
}
print(ru)
