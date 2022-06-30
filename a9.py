import random
import string
alphabet_upper_string=string.ascii_uppercase
alphabet_lower_string=string.ascii_lowercase
c=["1","2","3","4","5","6","7","8","9","0","10"]
a = list(alphabet_lower_string)
b = list(alphabet_upper_string)
d =["?",".","-","_","!","@","=","/","*","#","&"]
e=1
while e <= 4 :
    e=int(input("chnd hrf(az 4 bzrgtr vared conid)?"))
aa=random.choice(a)
bb=random.choice(b)
cc=random.choice(c)
dd=random.choice(d)
n=[aa,bb,cc,dd]
g=random.shuffle(n)
psw =n[0]+n[1]+n[2]+n[3]
while e>4 :
    aa=random.choice(a)
    bb=random.choice(b)
    cc=random.choice(c)
    dd=random.choice(d)
    x=[aa,bb,cc,dd]
    y = random.choice(x)
    psw =psw + y
    e = e-1
print(psw)  