class Shop:
    def __init__(self,buyer) -> None:
         self.buyer=buyer
         self.cart=[]
    def add_to_cart(self,item,price,quantity):
         self.cart.append({'Item_Name':item,'price':price,'quantity':quantity})
    
    def remove(self,item):
        for index,value in enumerate(self.cart):
            if value['Item_Name']==item:
                 del self.cart[index]
                 
                 
    def checkout(self,amount):
         total =0
         print(f"Greting from Super Shop, {self.buyer}\n")
         print(f"your shoping cart is :\n")
         for item in self.cart:
              print(f"{item}")
         for item in self.cart:
              total+=item['price']*item['quantity']
         if amount<total:
              print(f"your given amoout inefficient for checkout {amount}")
         else:
              amount-=total
              print(f"After  cehckout your chance is {amount}")
              
         
              
        
        


nihadgo75=Shop("Md.Nihad Hossain")
nihadgo75.add_to_cart("Nescafe",400,2)
nihadgo75.add_to_cart("Detergent",100,3)
nihadgo75.add_to_cart("Biscuit",75,5)
nihadgo75.remove('Detergent')
nihadgo75.checkout(3000)
         