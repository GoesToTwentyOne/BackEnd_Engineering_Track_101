x=[34,4,5,6,7,66,4,5,3,44,33,333]
y=[num for num in x if num%2==0 if num%6==0]
print(y)

#combination 
playes=["Sakib","Liton","Musfiq","Afif"]
ages=[34,46,34]
combination=[[player,age] for player in playes for age in ages]
print(combination)