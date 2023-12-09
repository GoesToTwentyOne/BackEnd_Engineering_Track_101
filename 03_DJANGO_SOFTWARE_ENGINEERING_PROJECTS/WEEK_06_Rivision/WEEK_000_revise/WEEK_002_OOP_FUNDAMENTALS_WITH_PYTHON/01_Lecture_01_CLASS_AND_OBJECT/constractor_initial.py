class Phone:
    manufacture_Rigiion='USA'

    def __init__(self,owner,brand,price,features) -> None:
        self.owner=owner
        self.brand=brand
        self.price=price
        self.features=features
        
    
    def calling(self):
        print("I calling you")
    def message(self,phone_num,message):
        msg=f"Sending To: {phone_num}  {message}-> Thanks to, You are doing good from nihadgo75"
        print(msg)


my_phone= Phone("Nihad Hossain","Samsung",39000,{'RAM':'8GB','Camera':"64 MP",'ROM':'128 GB'})
print(my_phone.owner,my_phone.brand,my_phone.features,my_phone.manufacture_Rigiion)
dad_phone= Phone("Kamal Hossain","Oppo",29000,{'RAM':'8GB','Camera':"64 MP",'ROM':'128 GB'})
print(my_phone.owner,my_phone.brand,my_phone.features,my_phone.manufacture_Rigiion)
gf_phone= Phone("Alex","IPHONE",1200000,{'RAM':'8GB','Camera':"64 MP",'ROM':'128 GB'})
print(my_phone.owner,my_phone.brand,my_phone.features,my_phone.manufacture_Rigiion)
my_phone.message('017788585',"I Love you jan")
dad_phone.message('017788585',"I Love you jan")
gf_phone.message('017788585',"I Love you jan")