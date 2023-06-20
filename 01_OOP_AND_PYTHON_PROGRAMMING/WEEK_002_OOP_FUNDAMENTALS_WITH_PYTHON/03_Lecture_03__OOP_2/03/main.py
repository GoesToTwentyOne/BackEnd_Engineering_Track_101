# class User:
#     def __init__(self,name,age,balance) -> None:
#         self.name=name
#         self._age = age
#         self.__balance=balance
#     @property
#     def salary(self):
#         return self.__balance
#     @salary.setter
#     def salary(self,value):
#         self.__balance += value
#         return 
# Nihad = User("Nihad",21,4500)
# print(Nihad.salary)
# Nihad.salary=4500
# print(Nihad.salary)


class Number:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def display(self):
        print(self.x)
        print(self.y)

    def __gt__(self, n):
        if self.x > n.x and self.y > n.y:
            return True
        else:
            return False

n1 = Number(200, 400)
n2 = Number(500, 700)
n3 = n1 > n2

if n3:
    print("n1 is greater")
else:
    print("n2 is greater")


        