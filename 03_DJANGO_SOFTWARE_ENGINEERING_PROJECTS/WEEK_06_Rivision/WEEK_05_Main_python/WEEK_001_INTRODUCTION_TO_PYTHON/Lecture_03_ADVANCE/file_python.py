with open('message.txt','w') as file:
    file.write("I love you jan")
with open('message.txt','a') as file:
    file.write("\nI love you jan")
with open('message.txt','r') as file:
    text=file.read()
    print(text)