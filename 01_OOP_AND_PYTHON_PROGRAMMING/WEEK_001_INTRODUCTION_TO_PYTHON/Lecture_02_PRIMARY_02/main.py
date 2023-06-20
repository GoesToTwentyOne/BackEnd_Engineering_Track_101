
"""
#L-1
def voter_Eligibility(x):
    if x>=18:
        print("You are eligible")
    else:
        print("you are under 18")

voter_Eligibility(10)
voter_Eligibility(20)
"""

#L-2
# def variadic(num1,num2=0,num3=1,*numbers):
#     print(num1)
#     print(num2)
#     print(num3)
#     for i in numbers:
#         print(i)
# variadic(num1=4)
# print('\n\n')
# variadic(num1=5,num3=5)
# print('\n\n')
# variadic(4,5,6,7,8,9,10,11,12)


# def all_possible_para(num1,num2,num3=0,*numbers,**kargs):
#     print(num1)
#     print(num2)
#     print(num3)
    

#     for i in numbers:
#         print(i)

#     for i,v in kargs.items():
#         print(i,v)
#L-3
def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")


numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])



# all_possible_para(num1=1,num2=45)
# print('\n\n')
# all_possible_para(50,60,70,80,90,78,78,78,78,78,title="Ni",title2="bye",title3="oi")
# print('\n\n')
# all_possible_para(50,60,70,80,90,78,78,78,78,78,title="Ni",title2="bye",title3="oi")