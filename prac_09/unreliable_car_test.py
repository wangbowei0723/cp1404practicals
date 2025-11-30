from unreliable_car import UnreliableCar

car = UnreliableCar("Unreliable", 100, 30)

for i in range(1, 11):
    distance = car.drive(10)
    print(f"Attempt {i}: Drove {distance}km")