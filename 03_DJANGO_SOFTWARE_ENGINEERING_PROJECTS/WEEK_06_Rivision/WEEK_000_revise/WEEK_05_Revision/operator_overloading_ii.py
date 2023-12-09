class IndianArmy:
    def __init__(self, tot_soldiers, avg_age, tot_tank):
        self.tot_soldiers = tot_soldiers
        self.avg_age = avg_age
        self.tot_tank = tot_tank
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} --> {self.tot_soldiers}:{self.avg_age}:{self.tot_tank}"

class BangladeshArmy:
    def __init__(self, tot_soldiers, avg_age, tot_tank):
        self.tot_soldiers = tot_soldiers
        self.avg_age = avg_age
        self.tot_tank = tot_tank
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} --> {self.tot_soldiers}:{self.avg_age}:{self.tot_tank}"



    def __add__(self, other):
        if isinstance(other, IndianArmy):
            total_soldiers = self.tot_soldiers + other.tot_soldiers
            avg_age = (self.avg_age + other.avg_age) / 2
            total_tanks = self.tot_tank + other.tot_tank
            return BangladeshArmy(total_soldiers, avg_age, total_tanks)
        else:
            raise ValueError("Unsupported operand types for +: BangladeshArmy and {}".format(type(other)))

india = IndianArmy(755555555555555, 35, 787878)
bangladesh = BangladeshArmy(455555555, 38, 888656)

print(india)
print(bangladesh)

combined_army = bangladesh + india
print(combined_army)
