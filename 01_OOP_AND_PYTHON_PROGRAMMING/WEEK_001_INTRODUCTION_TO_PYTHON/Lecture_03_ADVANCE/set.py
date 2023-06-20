A=[1,2,3,4,5,6,7,8]
print(A)
set_of_A=set(A)
print(set_of_A)
set_of_A.add(45)#doesn't maintain order and muteable
print(set_of_A)
set_of_A.remove(2)
print(set_of_A)
for item in set_of_A:
    print(item)
if 6 in A:
    print("Yes")

B={1,2,3,7,8,4434,6,}
C={78,5,23,1,2,4,5}
print(B&C)
print(B|C)