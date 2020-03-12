def preob(a):
    try:
        return float(a)
    except ValueError:
        print("не соответствуют типы данных")

c = preob("57658  ")
print(c)
