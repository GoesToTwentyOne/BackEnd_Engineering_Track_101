# a=[2,3,4,5,6,7,8]
# for i,v in enumerate(a):
#     print(i,v)
    
    
    
    
def insertion(a):
    for i in range(1, len(a)):
        index = i
        while index >= 1:
            if a[index - 1] > a[index]:
                temp = a[index - 1]
                a[index - 1] = a[index]
                a[index] = temp
                temp = a[index - 1]
                index -= 1
            else:
                break

a = [55, 6, 3, 2, 2]
insertion(a)

for num in a:
    print(num, end=" ")
