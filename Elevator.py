"""ELEVATOR"""
class Elevator:
    """Max"""
    def __init__(self, max_floor):
        """Mad"""
        self.current_floor = 1
        self.max_floor = max_floor
    def go_to_floor(self, floor):
        """Floor"""
        if 1 <= floor <= self.max_floor:
            self.current_floor = floor
        else:
            print("Invalid Floor!")
    def report_current_floor(self):
        """Current"""
        print(self.current_floor)
max_floor = int(input())
elevator = Elevator(max_floor)
while True:
    floor = input()
    if floor.lower() == "done":
        break
    else:
        elevator.go_to_floor(int(floor))
elevator.report_current_floor()
