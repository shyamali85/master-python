class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

def drive(self, hours):
    self.distance += self.speed * hours


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
      super().__init__(reg_number, max_speed)
      self.battery_capacity = battery_capacity


class GasolineCar(Car):
     def __init__(self, reg_number, max_speed, tank_volume):
        super().__init__(reg_number, max_speed)
        self.tank_volume = tank_volume


# MAIN
electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

# Set speeds
electric.speed = 100
gasoline.speed = 120

# Drive for 3 hours
electric.drive(3)
gasoline.drive(3)

print(f"{electric.reg_number} distance: {electric.distance} km")
print(f"{gasoline.reg_number} distance: {gasoline.distance} km")