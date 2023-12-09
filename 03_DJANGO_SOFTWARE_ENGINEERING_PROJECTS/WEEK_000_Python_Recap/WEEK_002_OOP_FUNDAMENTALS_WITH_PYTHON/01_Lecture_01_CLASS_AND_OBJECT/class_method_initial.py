class Phone:
    Model ='M31 Prime'
    Color="Black"
    Brand='Samsung'
    Ram='8 GB'
    Rom='!28 GB'
    Price=39000
    
    def calling(self):
        print("I calling you")
    def message(self,phone_num,message):
        msg=f"Sending To: {phone_num}  {message}-> Thanks to, You are doing good from nihadgo75"
        print(msg)
my_phone=Phone()
my_phone.calling()
my_phone.message('01773684304',"I love you")
my_phone=Phone()
my_phone.calling()
my_phone.message('01773684305',"I love you Jan")

