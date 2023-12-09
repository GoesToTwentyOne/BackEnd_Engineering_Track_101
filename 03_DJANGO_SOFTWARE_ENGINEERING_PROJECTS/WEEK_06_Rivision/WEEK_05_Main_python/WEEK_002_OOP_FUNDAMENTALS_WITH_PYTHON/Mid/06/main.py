from collections import Counter
N, M = map(int, input().split())
A = []
for i in input().split():
    A.append(int(i))

counts = Counter(A)
#print(counts)
for i in range(1, M+1):
    print(counts[i])#check with counter dictionary keys 
