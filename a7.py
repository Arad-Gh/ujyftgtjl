a =int(input(":"))
m =[]
b = 0
while a :
    m.append(int(a%10))
    a=int(a/10)
for i in range(9,0,-1):
    b = b + m[i]*(i+1)
w = b%11
if w<2 :
    m[9] == a%10
    print("Drste")
elif w>2:
    m[9] = 11 - a%10
    print("drste")
else :
    print("ghlte")