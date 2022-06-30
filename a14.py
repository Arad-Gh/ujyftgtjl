a="hello I am an student"
c=a.split(" ")
b={
    "I":" nm",
    "student":" zomahsnad",
    "hello":" malas",
    "an":" key",
    "am":""
}
x=""
for i in c:
    x=x+b[i]
mhl=[i for i in range(len(c))if c[i]=='I']
p=mhl[0]
c=x.split(" ")
e=p+4
for i in range(len(c)) :
    if 'nm'in c:
        if 'key' in c:
            c.insert(e,"matsah")
            break
        if 'key' not in c:
            sd=e-1
            c.insert(sd,"matsah")
            break
g=""
for i in range(len(c)):
    g =c[i]+" "+g
l=g[::-1]
print(l)