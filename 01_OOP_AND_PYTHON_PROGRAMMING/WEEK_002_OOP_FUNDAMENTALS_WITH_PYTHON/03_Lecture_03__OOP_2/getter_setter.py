class User:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money
    #getter
    @property
    def getAge(self):
        return self._age
    
    @property
    def getMoney(self):
        return self.__money
    
    @getMoney.setter
    def getMoney(self,value):
        if value<0:
            print("your value negtive")
        else:
            r=self.__money=self.__money + value
            return r
nihadgo75=User("Md. Nihad Hossain",21,15000)
print(nihadgo75.getAge)
print(nihadgo75.getMoney)
nihadgo75.getMoney=1500
print(nihadgo75.getMoney)
    
        