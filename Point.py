class clss:
    def __init__(self, xxx=0, yyy=0):
        self.set_coordinates(xxx, yyy)
    def set_coordinates(self, xxx, yyy):
        self.xxx = xxx
        self.yyy = yyy 
    def get_coordinates(self):
        return (self.xxx, self.yyy)
    def calculate_distance(self, other_point):
        return round(((other_point.xxx - self.xxx)**2 + (other_point.yyy - self.yyy)**2) ** 0.5, 2)
boss_xxx = float(input())
boss_yyy = float(input())
arth_xxx = float(input())
arth_yyy = float(input())
boss_point = clss(boss_xxx, boss_yyy)
arth_point = clss(arth_xxx, arth_yyy)
distance = boss_point.calculate_distance(arth_point)
print(distance)
