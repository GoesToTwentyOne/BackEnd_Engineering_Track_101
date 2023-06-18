N = int(input())
A = []
for i in input().split():
    A.append(int(i))
max_operations = 0
#all() returns true
all_even = all(num % 2 == 0 for num in A)
while all_even:
    A = [num // 2 for num in A]
    max_operations += 1
    all_even = all(num % 2 == 0 for num in A)
print(max_operations)
