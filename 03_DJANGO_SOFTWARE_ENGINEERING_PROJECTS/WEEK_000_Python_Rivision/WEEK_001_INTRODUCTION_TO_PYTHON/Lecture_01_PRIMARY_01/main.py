#L-01
print("Copa python copa")
print("Hi python")



#L-02
x=20
name="Nhad Hossain"
interest_Rate=4.5
district="Every thing is possible"
is_single=True
is_Double=False


#single line comment = ctrl + / 
#doc string =alt + shift + A

print(x,name,district,is_single,is_Double)
print(type(x))
print(type(interest_Rate))
print(type(is_single))
print(is_Double)


#f sting 
text= f"My name is {name}. Inspiration {district}, I'm single {is_single}"
print(text)



#L-3
input_data=input("Give me some money :  ")
print(input_data)

x=int(input("Give number 1:"))
y=int(input("give number 2:"))
print("Total ",x+y)



#L-4
print(106/3)
print(106%3)
print(106//3)



#L-5
x=10
if x<5:
    print("x is grater")
elif x==100:
    print("x is 10")
else:
    print("x is 20")

boss= False

if boss is True:
    print("boss is here")
elif boss is not True:
    print("boss isn't here")
else:
    print("we are not ready")



#L-6
i=0
while i<=10:
    i+=1
    if i%2==1:
        continue
    print(i)

x=[1,2,3,4,5]
for i in x:
    print(i)

y="Nihad"
for i in y:
    print(i)

for i in range(1,10,2):
    print(i)

ff=[45,78,9,23,3,56]
for i,v in enumerate(ff):
    print(i,v) 