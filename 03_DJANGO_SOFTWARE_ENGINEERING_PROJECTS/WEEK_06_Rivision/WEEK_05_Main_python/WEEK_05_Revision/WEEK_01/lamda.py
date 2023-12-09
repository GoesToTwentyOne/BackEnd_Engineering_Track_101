add=lambda x,y:x+y
print(add(23,45))
l=[3,4,54,5,6,89,87]


doubleit=lambda x:x*2>5
print(list(map(doubleit,l)))

actors=[
    {'Name':"Alex",'Age':21},
    {'Name':"Alex2",'Age':23},
    {'Name':"Alex3",'Age':28},
    {'Name':"Alex4",'Age':29},
    {'Name':"Alex5",'Age':20},
    {'Name':"Alex6",'Age':19}
]
print(list(filter(lambda actor:actor['Age']>23,actors)))





