# balance=5000
# #ocure global func modify error
# def buing_merge(item,price):
#     print(f"your balance before buying : {balance}")
#     balance=balance-price
#     print(f"your balance after  buying {item}: {balance}")

# buing_merge("Spectacles",1000)


balancein=5000
#ocure global func modify error
def buing_mergein(item,price):
    global balancein
    print(f"your balance before buying : {balancein}")
    balancein=balancein-price
    print(f"your balance after  buying {item}: {balancein}")

buing_mergein("Spectacles",1000)