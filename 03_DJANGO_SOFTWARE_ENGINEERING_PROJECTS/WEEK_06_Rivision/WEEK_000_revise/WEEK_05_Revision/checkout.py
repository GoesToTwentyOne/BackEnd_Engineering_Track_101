class SimpleShop:
    def __init__(self,customer):
        self.customer = customer
        self.cart=[]
    def add_to_cart_item(self, item, quantity,price):
        product = {'item': item, 'quantity':quantity, 'price':price}
        self.cart.append(product)
    def view_cart_item(self):
        print(f"{self.customer} cart is :\n")
        for item in self.cart:
            print(item)
    def checkout(self,balance):
        total_cost=0
        for item in self.cart:
            total_cost+=item['price']*item['quantity']
        if total_cost> balance:
            print(f"{self.customer} please enter current balance")
        elif total_cost<balance:
            print(f"your payment {total_cost} successfully. {self.customer} your changes will be {balance-total_cost}")
        else:
            print(f"{self.customer} your payment {total_cost} successfully.")
    def remove_item(self, item_to_remove):
         for i in self.cart:
             if  i['item']==item_to_remove:
                 self.cart.remove(i)

            
Nihad=SimpleShop(customer="Nihad")
Nihad.add_to_cart_item(item="Sunglasses",quantity=1,price=500)
Nihad.add_to_cart_item(item="Detergent",quantity=1,price=80)
Nihad.add_to_cart_item(item="Coffe",quantity=1,price=300)
Nihad.add_to_cart_item(item="Tooth Brush",quantity=1,price=160)
Nihad.view_cart_item()
Nihad.checkout(5000)
Nihad.checkout(1040)
Nihad.remove_item(item_to_remove="Coffe")
Nihad.view_cart_item()
  
        