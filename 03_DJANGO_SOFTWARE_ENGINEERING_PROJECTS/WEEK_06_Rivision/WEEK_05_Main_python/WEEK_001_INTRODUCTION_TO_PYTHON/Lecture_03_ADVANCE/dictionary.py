A={'Name':'Md. Nihad Hossain','Age':21,'Country':'Bangladesh','Expert':"Computer Programming"}
print(A)
print(A['Name'])
A['fav']='Python & Golang'
print(A)
A["Age"]=22
print(A.keys())
print(A.values())
print('\n \n')


for key,value in A.items():
    print(key,value)