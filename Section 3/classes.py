
"""
class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]
    def __repr__(self):
        return f'<Garage {self.car}>'
    def __str__(self):
        return f'Garage  with {len(self)}'
volkswagon = Garage()
volkswagon.cars.append('Jetta')
volkswagon.cars.append('Gulf')

for car in volkswagon:
    print(car)

print(volkswagon[0])

"""

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
    def __getitem__(self, i):
        return self.players[i]
    def __len__(self):
        return len(self.players)
    def __repr__(self):
        return 'Club {}: {}'.format(self.name, self.players)
    def __str__(self):
        return 'Club {} with {} players'.format(self.name, len(self))

