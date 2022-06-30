import json
import emoji
import sys

f=open("a11.json","r")
di=f.read()
dicti=json.loads(di)
f.close()

def getList(dicti):
    return list(dicti.keys())
keys=getList(dicti)

darseee_morednazar = input("edit ya didn ya ezafe krdn yek dars=esme dars ,didan kol list=all : ")
if darseee_morednazar=="all":
    f=open("a11.json","r")
    x=f.read()
    print(x)
    sys.exit()

editYAdidn= input("edit ya ezafe krdn dars =e , didn etelaat marboot be dars =d : ")

if editYAdidn == "e" or "d":
    if darseee_morednazar in keys:
        if editYAdidn =="e":
            t =input("tarikh: ")
            r=input("rooz: ")
            s=input("saat: ")
            dicti[darseee_morednazar]=t+"-"+r+"-"+s
        if editYAdidn == "d":
            print(dicti[darseee_morednazar])          
    else:
        while not editYAdidn in keys :
            print("moredi baraie in dars sabt nshde.")
            t =input("tarikh: ")
            r=input("rooz: ")
            s=input("saat: ")
            dicti[darseee_morednazar]=t+" , "+r+" , "+s
            print("be list ezafe shod.")
            y=json.dumps(dicti)
            with open("a11.json","w") as esm_darsha:
                esm_darsha.write(y)
            break
else :
    print("ERROR 404"+ emoji.emojize(":zipper-mouth_face:"))

a=input("didan kol list=a ,exit=bghie dkme ha: ")

if a=="a":
    print(dicti)
    y=json.dumps(dicti)
    with open("a11.json","w") as esm_darsha:
        esm_darsha.write(y)
        sys.exit()
else:
    y=json.dumps(dicti)
    with open("a11.json","w") as esm_darsha:
        esm_darsha.write(y)
        sys.exit()