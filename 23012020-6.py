def squer(x):
    return x ** 2

print(squer(4)) #Выводится квадрат четырех

def stroka(y):
    print(y)

stroka("Hay!") #Выводится строка Hay!

def parametr(a,b,c,d=100,e=200):
    return a + b + c *d * e

print(parametr(10, 11, 12))
"""
    в этой строке выводится
    :результатт функции parametr
    """

def devide(f):
    return f * 2
def result(g):
    return g / 4

h = devide(4654)
i = result(h)
print(i)
"""Здесь выводится
    результат, полученный
    :делением результата первой функции на 4
    """

def returning(f):
    try:
        return float(f)
    except ValueError:
        print ("Отстой")
g = returning("11")
print(g)
""" В этой проге
    выводится ошибка.
    Сама прога делает что-то с
    двумя функциями.
    """

        


