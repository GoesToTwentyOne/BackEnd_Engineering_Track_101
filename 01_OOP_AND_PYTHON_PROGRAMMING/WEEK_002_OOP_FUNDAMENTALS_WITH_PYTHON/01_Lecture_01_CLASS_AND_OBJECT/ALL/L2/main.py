from typing import Self


class Laptop:
    brand="Asus"
    def gloabal(self):
        print("USA version")
    def sendVIMyasus(self,port,message):
        print(f'My port NO : {port},secret message for you {message}')

L1= Laptop()
L1.gloabal()
L1.sendVIMyasus(4569,"I love you")
    