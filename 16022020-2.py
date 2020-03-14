class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} to {}
              """.format(self.width,
                         self.len))

my_shape = Shape(21, 55)
my_shape.print_size()

my_shape2 = Shape(80, 175)
my_shape2.print_size()

class Square(Shape):
    pass

a_square = Square(20, 20)
a_square.print_size()
   
