with open('hi.txt','w') as file:
    file.write("hi")
with open('hi.txt','r') as file:
    txt=file.read()
    print(txt)