class Shape():
    def what_am_i(self):
        print('I am a figure')
        
class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

class Rectangle(Shape):
    pass
    

a_square = Square(100)
print(a_square.s1)

a_rectangle = Rectangle
print(a_square.s1)

a_square.what_am_i()
