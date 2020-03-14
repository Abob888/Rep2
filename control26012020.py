a = ["Queen", "Muse", "Sting"]
print(a) # Выводит любимы группы (зад.1)

b = [(34, 45),
     (56, 71),
     (25, 93)]
print(b) # Координаты любимых мест (зад.2)

c = {"name": "Aleks",
     "age": 36,
     "programmer": True,
     "Land": "Russia"
}
print(c) # Словарь

d = input("Your data: ")
if d in c:
    e = c[d]
    print(e)
else:
    print("XXXXXXXX")
    """Выводит данные из
    предыдущего словаря
    по запросу
    """

f = {"Queen":
     ["I want it all",
      "Who wants to live forever",
      "Mother Love"],
     "Muse":
     ["Histeria",
      "Feelig good",
      "Uprising"],
     "Sting":
     ["Desert Rose",
      "Englishman in New York",
      "Shape of my heart"]
}
print(f) # БД любимых песен любимых групп


     
    


