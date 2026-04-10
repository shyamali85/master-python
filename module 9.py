class Car:
def __init__(self, registration_number, maximum_speed):
self.registration_number = registration_number
self.maximum_speed = maximum_speed
self.current_speed = 0
self.travelled_distance = 0

def accelerate(self, change):
self.current_speed += change

if self.current_speed > self.maximum_speed:
self.current_speed = self.maximum_speed
if self.current_speed < 0:
self.current_speed = 0

def drive(self, hours):
self.travelled_distance += self.current_speed * hours


# Create cars
cars = []
for i in range(1, 11):
max_speed = random.randint(100, 200)
car = Car(f"ABC-{i}", max_speed)
cars.append(car)


# Race loop
race_on = True
while race_on:
for car in cars:
change = random.randint(-10, 15)
car.accelerate(change)
car.drive(1)

if car.travelled_distance >= 10000:
race_on = False


# Print results
for car in cars:
print(car.registration_number,
car.maximum_speed,
car.current_speed,
car.travelled_distance)