import random

class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance = 0

    def drive(self):
        self.distance += self.speed


class Race:
     def __init__(self, name, distance, cars):
         self.name = name
         self.distance = distance
         self.cars = cars

     def hour_passes(self):
         for car in self.cars:
           change = random.randint(-10, 15)
           car.speed = max(0, car.speed + change)
           car.drive()

     def print_status(self):
         print("\nCar\tSpeed\tDistance")
         for car in self.cars:
             print(f"{car.name}\t{car.speed}\t{car.distance}")

     def race_finished(self):
       for car in self.cars:
          if car.distance >= self.distance:
              return True
       return False


# MAIN
cars = []
for i in range(10):
    cars.append(Car(f"Car{i+1}"))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
      race.hour_passes()
      hours += 1

      if hours % 10 == 0:
         race.print_status()

print("\nRace finished!")
race.print_status()