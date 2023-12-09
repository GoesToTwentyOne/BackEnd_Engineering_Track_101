class Shop:
    shopping_cart=[]   #class attribute shared for all
    def __init__(self,buyer) -> None:
        self.buyer=buyer
    def add_to_cart(self,item):
        self.shopping_cart.append(item)
nihadgo75 = Shop("Md. Nihad Hossain")
nihadgo75.add_to_cart("phone")
nihadgo75.add_to_cart("Wallet")
nihadgo75.add_to_cart("Blanket")
print(nihadgo75.shopping_cart)
alex = Shop("Alex Goot")
alex.add_to_cart("Lip Stick")
alex.add_to_cart("Foundation MakeUp")
alex.add_to_cart("Blanket")
print(alex.shopping_cart)


class Walton:
    outlet="Saidpur Branch"
    def __init__(self,buyer) -> None:
        self.buyer=buyer
        self.shopping_cart=[]#instance attribute work for diff instance
    def add_to_cart(self,item):
        self.shopping_cart.append(item)



nihadgo75 = Walton("Md. Nihad Hossain")
nihadgo75.add_to_cart("Fridge")
nihadgo75.add_to_cart("Iron")
nihadgo75.add_to_cart("Washing Machine")
print(nihadgo75.shopping_cart)
alex = Walton("Alex Goot")
alex.add_to_cart("Air Conditionar")
alex.add_to_cart("Oven")
alex.add_to_cart("Rice Cooker")
print(alex.shopping_cart)
        
        
        