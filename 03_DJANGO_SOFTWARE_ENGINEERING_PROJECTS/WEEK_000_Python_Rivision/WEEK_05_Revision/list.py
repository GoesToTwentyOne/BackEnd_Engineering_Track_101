x=[3,4,5,5,6,7,78,8,8,9,9,99]
print(x[::-1])



numbers=[3,4,54,5,6,22,3,66,78,9,89,90]
od_num_5_divisible=[num for num in numbers if num %2==1 if num%5==0]
print(od_num_5_divisible)

players=['Sakib','Musfiq','Liton']
ages=[33,76,67]

combinations=[[player,age] for player in players for age in ages]
print(combinations)