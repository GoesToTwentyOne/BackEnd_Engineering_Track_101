S = input()  
count_L = 0
count_R = 0
balanced_strings = []
#print(balanced_strings)
for c in S:
    if c == 'L':
        count_L += 1
        #print(count_L)
    else:  # c == 'R'
        count_R += 1
        #print(count_R)
    if count_L == count_R:
        #print(count_L == count_R)
        balanced_strings.append(S[:count_L + count_R])
        #print(balanced_strings)
        S = S[count_L + count_R:]
        #print(S)
        count_L = 0
        count_R = 0
print(len(balanced_strings))
for s in balanced_strings:
    print(s)
