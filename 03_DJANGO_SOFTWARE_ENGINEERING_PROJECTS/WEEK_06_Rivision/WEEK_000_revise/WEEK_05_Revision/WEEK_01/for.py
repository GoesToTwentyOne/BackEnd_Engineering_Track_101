x=[5,10,14,5,5]
for i in range(0,len(x),1):
    x[i]=i+1
print(x)


sum=0
for i in x:
    sum+=i
print(sum)
   
    
name="Md. Nihad Hossain"
for char in name:
    print(char)


for i,v in enumerate(x,len(x)):
    print(i,v)