class Phone:
    brand = "samsung"
    ram=6
    features=["camera","Charger"]
    def callMe(self):
        print("I call you !later")
    def messageMe(self,text,number):
        return f"Sending a message From {number} to 456888  {text}"
    
my_Phone=Phone()
my_Phone.callMe()
x=my_Phone.messageMe("I Love you",45455454)
print(x)