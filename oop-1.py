class Orange():
    def __init__(self, w, c):
        '''Вес в граммах'''
        self.weight = w
        self.color = c
        self.mold = 0
        print('Gemacht!')

    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(6, 'apelsin')
print(orange.mold)
orange.rot(10, 33)
print(orange.mold)
