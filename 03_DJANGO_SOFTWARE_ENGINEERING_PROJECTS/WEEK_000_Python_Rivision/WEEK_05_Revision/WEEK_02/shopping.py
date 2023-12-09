class Shop:
    def __init__(self,name) -> None:
        self.name=name
        self.cart=[]
    
    def add_to_cart(self,item,price,quantity):
        self.cart.append({'item':item,'price':price,'quantity':quantity})
    
    def cart_view(self):
        for item in self.cart:
            print(item)
    def remove_item(self,item):
        for i in self.cart:
            if i['item']==item:
                self.cart.remove(i)
        print("your item out of cart")
            
            
    
    def check_out(self,amount):
        total=0
        for item in self.cart:
            total+=item['price']*item['quantity']
        if amount<total:
            print(f"your balance is insufficient {total}, you need to pay also {total-amount}")
        else:
            print(f"your balance is sufficient {total}, your change is {amount-total}")
person=Shop("A")
person.add_to_cart("Potato",35,5)
person.add_to_cart("Brinjal",60,3)
person.add_to_cart("Guard",35,2)
person.add_to_cart("Wheat",35,10)
person.cart_view()
person.remove_item('Guard')
person.cart_view()
person.check_out(4500)


            
        