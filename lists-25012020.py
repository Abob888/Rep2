fruit = list()
print(fruit)

fruit = ["apple", "grape", "banana"]
fruit.append("orange")
fruit.append("cherry")
fruit.append(True)
fruit.append(100)
fruit.append(1.1)
fruit.append("Маракуя")
print(fruit[0])
print(fruit[3])
print(fruit[5])

colors = ["синий", "зеленый", "красный"]
print(colors)
colors[2] = "желтый"
print(colors)
item = colors.pop()
print(item)
print(colors + fruit)
print("зеленый" in colors)
print("black" not in colors)
print(len(colors + fruit))

guess = input("Угадаете цвет: ")
if guess in colors:
    print("Yes!")
else:
    print("Wrong!")
    
