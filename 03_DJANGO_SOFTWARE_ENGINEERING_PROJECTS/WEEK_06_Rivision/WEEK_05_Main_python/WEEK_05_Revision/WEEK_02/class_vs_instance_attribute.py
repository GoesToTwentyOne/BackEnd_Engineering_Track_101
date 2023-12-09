class Shop:
    shopingmall="Saidpur Plaza"
    cart=[]
    def __init__(self,buyer) -> None:
        self.buyer=buyer
    def add_to_cart(self,item):
        self.cart.append(item)
    def Total_item(self):
        print(self.cart)

myShoping=Shop("A")
myShoping.add_to_cart("X")
myShoping.add_to_cart("Y")
myShoping.add_to_cart("Z")
myShoping.Total_item()

ABC=Shop("ABC")
ABC.add_to_cart("A")
ABC.add_to_cart("B")
ABC.add_to_cart("C")
ABC.Total_item()
class ShopTwo:
    shopingmall="Saidpur Plaza"
    
    def __init__(self,buyer) -> None:
        self.buyer=buyer
        self.cart=[]
    def add_to_cart(self,item):
        self.cart.append(item)
    def Total_item(self):
        print(self.cart)

myShoping=ShopTwo("A")
myShoping.add_to_cart("X")
myShoping.add_to_cart("Y")
myShoping.add_to_cart("Z")
myShoping.Total_item()

ABC=ShopTwo("ABC")
ABC.add_to_cart("A")
ABC.add_to_cart("B")
ABC.add_to_cart("C")
ABC.Total_item()
