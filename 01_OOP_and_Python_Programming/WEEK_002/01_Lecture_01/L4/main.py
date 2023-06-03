class Shopping:
    cart=[]
    def __init__(self,buyer):
        self.buyer=buyer
    def addToCart(self,items):
        self.cart.append(items)
Alex = Shopping("Alex")

Alex.addToCart("Trouser")
Alex.addToCart("Yoyo")
Alex.addToCart("Plazu")
print(Alex.cart)
Bob = Shopping("Bob")
Bob.addToCart("Watch")
Bob.addToCart("T-Shirt")
Bob.addToCart("Half-Pant")
print(Bob.cart)
