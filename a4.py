def zarb(a,b):
    print(a*b)
def jam(a,b):
    print(a+b)
def menha(a,b):
    print(a-b)
def taghsim(a,b):
    print(a/b)
a=int(input(": "))
c=input("+  -  *  / :")
b=int(input(": "))
if c == "+" :
    jam(a,b)
if c == "*" :
    zarb(a,b)
if c == "-" :
    menha(a,b)
if c == "/" :
    taghsim(a,b)