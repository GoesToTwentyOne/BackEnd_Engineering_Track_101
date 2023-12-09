class Shopping:
    
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]
    def addToCart(self,items):
        self.cart.append(items)
Alex = Shopping("Alex")

Alex.addToCart("Trouser")
Alex.addToCart("Yoyo")
Alex.addToCart("Plazu")
Bob = Shopping("Bob")
Bob.addToCart("Watch")
Bob.addToCart("T-Shirt")
Bob.addToCart("Half-Pant")
print(Alex.cart)
print(Bob.cart)
