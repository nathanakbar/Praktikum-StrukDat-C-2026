class MyCar:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color
        
    def introduce_self(self):
        print(f"My name car is"+{self.name}, "My year car is"+{self.year}, "My color car is"+{self.color})
    
    def change_name(self, new_name):
        self.name = new_name
        print(f"My new color car is"+{self.name})
        
p1 = MyCar("Mustang", "2007", "black")
p2 = MyCar("ford", "2000", "red")
p3 = MyCar("Tesla", "2019", "white")

print(p1.name, p2.name, p3.name)
print(p1.year, p2.year, p3.year)
print(p1.color, p2.color, p3.color)
p1.name = "bugatti"


        