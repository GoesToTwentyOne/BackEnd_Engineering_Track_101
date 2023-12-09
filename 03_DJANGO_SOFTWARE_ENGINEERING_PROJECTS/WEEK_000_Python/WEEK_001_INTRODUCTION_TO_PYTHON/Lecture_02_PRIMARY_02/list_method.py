xi= [4,5,6,7,9,5,55,5,54,33,3,4,544,8]
xii=[45,77,78]

xi.append(23)
xii.extend(xi)
print(xii)
xi.insert(3,6666)
print(xi)
if 9 in xi:
    xi.remove(9)
print(xi)
xi.pop()
print(xi)