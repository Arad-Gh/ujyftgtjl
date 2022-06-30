import random
skq = ["sang" , "kaqaz" , "qeichi"]
x = random.choice(skq)
a = input("sang , kaqaz , qeichi :" )
print(x)
if x == a :
    print("draw")
if x==skq[0] :
    if a == "kaqaz":
        print("lose")
    if a == "qeichi" :
        print("win")
if x==skq[1] :
    if a == "sang":
        print("win")
    if a == "qeichi" :
        print("lose")
if x==skq[2] :
    if a == "sang":
        print("lose")
    if a == "kaqaz":
        print("win")