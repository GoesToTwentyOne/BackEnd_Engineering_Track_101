from collections import defaultdict
N = int(input())
A = []
for i in input().split():
    A.append(int(i))
mp = defaultdict(int)
for i in A:
    mp[i] += 1
sum = 0
for key, value in mp.items():
    if value < key:
        sum += value
    elif value > key:
        sum += (value - key)
print(sum)
