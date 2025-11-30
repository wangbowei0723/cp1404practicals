from car import Car
from random import randint

class UnreliableCar(Car):
    """Represent a Car object."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """generate a random number, drive the car if number < reliability"""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return 0

        drive_distance = super().drive(distance)
        return drive_distance