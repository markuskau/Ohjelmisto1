class Hissi:
    def __init__(self, lower_floor, upper_floor):
        self.lower_floor = lower_floor
        self.upper_floor = upper_floor
        self.current_floor = lower_floor

    def upper_floor(self):
        if self.current_floor < self.upper_floor:
            self.current_floor += 1
            print(f"The elevator is now on the floor: {self.current_floor}")

    def lower_floor(self):
        if self.current_floor > self.lower_floor:
            self.current_floor -= 1
            print(f"The elevator is now on the floor: {self.current_floor}")

    def move_elevator(self, target_floor):
        if target_floor < self.lower_floor or target_floor > self.upper_floor:
            print("Error: Target floor is out of range.")
            return

        print(f"Moving the elevator to the floor: {target_floor}")
        while self.current_floor < target_floor:
            self.upper_floor()
        while self.current_floor > target_floor:
            self.lower_floor()

h = Hissi(1,10)

h.move_elevator(5)
h.move_elevator(1)

