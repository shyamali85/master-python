class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
      self.bottom_floor = bottom_floor
      self.top_floor = top_floor
       self.elevators = []

      # Create elevators and store them in a list
       for i in range(num_elevators):
         self.elevators.append(Elevator(bottom_floor, top_floor))


    def run_elevator(self, elevator_number, destination_floor):
     elevator = self.elevators[elevator_number]
     elevator.go_to_floor(destination_floor)