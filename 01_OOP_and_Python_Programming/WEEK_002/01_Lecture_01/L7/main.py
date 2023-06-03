from msilib.text import tables


class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def addToCart(self,item_name,quantity,price):
        your_cart={'Item_Name':item_name,'Quantity':quantity,'Price':price}
        self.cart.append(your_cart)
    def checkOutPreview(self):
        for item in self.cart:
            print(f"{self.name}, {item['Item_Name']}, {item['Quantity']}, {item['Price']}\n")
    def checkout(self,amount):
        total =0
        for item in self.cart:
            total+=item['Price']*item['Quantity']
        if total>amount:
            print(f"Total : {total}, After shoping ,you have to pay {total-amount}")
        else:
            print(f"After shoping ,you get  {amount-total},Thanks for shopping")


Nihad= Shopping("Nihad")
Nihad.addToCart(item_name="Chipse",quantity=1,price=45)
Nihad.addToCart(item_name="Chipse",quantity=1,price=45)
Nihad.addToCart(item_name="Chipse",quantity=1,price=45)
Nihad.addToCart(item_name="Chipse",quantity=1,price=45)
Nihad.addToCart(item_name="Chipse",quantity=1,price=45)
Nihad.addToCart(item_name="Chipse",quantity=1,price=45)
Nihad.checkOutPreview()
Nihad.checkout(4000)


Alex= Shopping("Alex")
Alex.addToCart(item_name="Chipse",quantity=1,price=450)
Alex.addToCart(item_name="Chipse",quantity=1,price=45)
Alex.addToCart(item_name="Chipse",quantity=1,price=450)
Alex.addToCart(item_name="Chipse",quantity=1,price=45)
Alex.addToCart(item_name="Chipse",quantity=1,price=45)
Alex.addToCart(item_name="Chipse",quantity=1,price=450)
Alex.checkOutPreview()
Alex.checkout(400)


