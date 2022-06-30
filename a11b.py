import json
with open("a10.json","r") as myfile :
    json.loads(myfile)

b=myfile.keys()

w = input("dars: ")
if w in b:
    while w in b:
        print(myfile[w])
else:
    while not w in b :
        print("etelaati darbare in dars sabt nshde")
        x=input("rooz: ")
        q=input("saat: ")
        myfile[w]=x+"-"+q
        print("It's OK")
import json
b=json.dumps(myfile)
with open("a10.json","w") as myfile :
    myfile.write()