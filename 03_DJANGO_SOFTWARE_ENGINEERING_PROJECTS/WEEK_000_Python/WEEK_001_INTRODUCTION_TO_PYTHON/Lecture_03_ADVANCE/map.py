
from os import name


xi=[45,6,7,3,8,9,3,22,2,5,57,9]
print(xi)
double=map(lambda x: x*2,xi)
print(list(double))



actors=[
    {'name':'Sunehra','age':25},
    {'name':"Katrina",'age':27},
    {'name':"Karina",'age':25},
    {'name':"Sibila Nur",'age':25},
    {'name':"Pori Moni",'age':28},
    {'name':"Alex",'age':52},
    {'name':"Sunny Leon",'age':25},
    {'name':"Jarin Khan",'age':30},
    {'name':"Mahjabin",'age':25},
    {'name':"Jacika",'age':25},
]
actor25=filter(lambda actor: actor['age']==25,actors )
print(list(actor25))