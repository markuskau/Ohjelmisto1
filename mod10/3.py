class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor

    def upper_floor(self):
        if self.current_floor < self.highest_floor:
            self.current_floor += 1
            print(f"The elevator is now on the floor: {self.current_floor}")

        else:
            print("Elevator is already on the top floor")

    def lower_floor(self):
        if self.current_floor > self.lowest_floor:
            self.current_floor -= 1
            print(f"The elevator is now on the floor: {self.current_floor}")

        else:
            print("Elevator is already on the bottom floor")

    def move_elevator(self, target_floor):
        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print("Error: Target floor is out of range.")
            return

        print(f"Moving the elevator to the floor: {target_floor}")
        while self.current_floor < target_floor:
            self.upper_floor()
        while self.current_floor > target_floor:
            self.lower_floor()

class House:
    def __init__(self, lowest_floor, highest_floor, elevators_count):
        self.elevators = [Elevator(lowest_floor, highest_floor) for _ in range(elevators_count)]

    def use_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Use elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].move_elevator(target_floor)

        else:
            print("Error: Elevator number out of range.")

    def firealarm(self):
        print("Firealarm! All the elevators must be moved to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Moving the elevator {i} to bottom floor.")
            elevator.move_elevator(self.lowest_floor)





house = House(1, 10, 3)

house.use_elevator(0, 5)
house.use_elevator(1, 7)
house.use_elevator(2, 3)
house.use_elevator(0, 1)

house.firealarm()



