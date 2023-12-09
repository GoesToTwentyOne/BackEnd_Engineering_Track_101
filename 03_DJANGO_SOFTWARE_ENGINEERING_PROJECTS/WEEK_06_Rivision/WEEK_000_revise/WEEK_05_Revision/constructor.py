class Pen:
    def __init__(self,owner,brand,price,color):
        self.owner=owner
        self.brand=brand
        self.price=price
        self.color=color
    def write(self,owner):
        print(f"This is {self.owner} pen")
        
my_pen=Pen(owner="Nihad",brand="Matador",price=12,color="Green")
my_pen.write(my_pen.owner)
my_mom_pen=Pen(owner="Tajnin Ara",brand="Apex Gel",price=120,color="Black")
my_mom_pen.write(my_mom_pen.owner)
my_dad_pen=Pen(owner="Mr. Kamal",brand="Good Luck Gel",price=126,color="Red")
my_dad_pen.write(my_dad_pen.owner)