def even_odd():
    n = input("Введите число: ")
    n = int(n)
    if n % 2 == 0:
        print("n - четное")
    else:
        print("n - нечетное")
for i in range(10):
    even_odd()

