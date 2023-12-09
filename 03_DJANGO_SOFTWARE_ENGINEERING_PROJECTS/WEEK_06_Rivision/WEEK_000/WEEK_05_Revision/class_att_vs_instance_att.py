class ShopService:
    def __init__(self,customer,item,price):
        self.customer = customer
        self.item = item
        self.price = price
        self.cart=[]
    def add_to_cart(self,item):
        self.cart.append(item)
    def get_cart(self,customer):
        print(f"This is {self.customer} shopping cart with {self.cart} items")


Alex=ShopService(customer="Alex",item="Sunglass",price=1300)
Alex.add_to_cart(Alex.item)
Nana=ShopService(customer="Nana",item="Lip Stick",price=450)
Nana.add_to_cart(Nana.item)
Neha=ShopService(customer="Neha",item="Bag",price=1100)
Neha.add_to_cart(Neha.item)
Alex.get_cart(Alex.customer)
Nana.get_cart(Nana.customer)
Neha.get_cart(Neha.customer)
        