class Horse():
    def __init__(self, color, sex, rider):
        self.color = color
        self.sex = sex
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

man = Rider('Pol')
anml = Horse('blue', 'girl', man)
print(anml.rider.name)
