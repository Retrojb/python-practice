class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the Garage')
        self.cars.append(car)


    @staticmethod
    def count_of_cars(car):
        if car is None:
            raise ValueError('No cars exist in the garage')


volkswagon = Garage()
car = Car('Volkswagon', 'Jetta')
volkswagon.add_car(car)
print(len(volkswagon))
car_list = Garage.count_of_cars(car)
print(car_list)


