import json
import turtle
import sys
import turtle

turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.bgpic("Motion_Made_Free_Loop_animated_background_Education_Study_Table_Teacher_Day_Back_to_School (1).gif")

f=open("a11.json","r")
di=f.read()
dicti=json.loads(di)
f.close()
def getList(dicti):
    return list(dicti.keys())
keys=getList(dicti)

def kolesh():
    darseee_morednazar = turtle.textinput(" ","edit ya didn ya ezafe krdn yek dars=esme dars ,didan kol list ya hazf yek dars=all : ")
    if darseee_morednazar=="all":
            f=open("a11.json","r")
            x=f.read()
            turtle.penup()
            turtle.goto(-300,0)
            turtle.pendown
            turtle.write(x,font=("Bold",13,'normal'))
            turtle.penup()
            turtle.goto(-100,0)
            turtle.pendown
            q=turtle.textinput(" ","kodoom darsro mikhai hazf koni?(age nmikhay 'n' ro bzn)")
            if q in keys :
                del dicti[q]
                y=json.dumps(dicti)
                with open("a11.json","w") as esm_darsha:
                    esm_darsha.write(y)
            if q not in keys:
                turtle.write("Hmchin darsi dar list vojood nadare")
            if q=="n":
                pass
            s=turtle.textinput("","car dige ei dari?=Y or N")
            while s=="Y":
                turtle.clear()
                kolesh()
            if s=="N" :
                sys.exit()
    editYAdidn= turtle.textinput(" ","edit ya ezafe krdn dars =e , didn etelaat marboot be dars =d : ")
    if editYAdidn == "e" or "d":
        if darseee_morednazar in keys:
            if editYAdidn =="e":
                t =turtle.textinput("etelaat marboot be dars ra vared konid : ","tarikh: ")
                r=turtle.textinput("etelaat marboot be dars ra vared konid : ","rooz: ")
                s=turtle.textinput("etelaat marboot be dars ra vared konid : ","saat: ")
                dicti[darseee_morednazar]=t+"-"+r+"-"+s
                y=json.dumps(dicti)
                with open("a11.json","w") as esm_darsha:
                    esm_darsha.write(y)
            if editYAdidn == "d":
                turtle.write(dicti[darseee_morednazar],font=("Bold",15,'normal'))         
        else:
            while not editYAdidn in keys :
                turtle.write("moredi baraie in dars sabt nshde.")
                t =turtle.textinput("etelaat marboot be dars ra vared konid : ","tarikh: ")
                r=turtle.textinput("etelaat marboot be dars ra vared konid :","rooz: ")
                s=turtle.textinput("etelaat marboot be dars ra vared konid :","saat: ")
                dicti[darseee_morednazar]=t+"-"+r+"-"+s
                turtle.write("be list ezafe shod.")
                y=json.dumps(dicti)
                with open("a11.json","w") as esm_darsha:
                    esm_darsha.write(y)
                break
    break1=turtle.textinput(" ","baraye edame enter ro bznid")
    turtle.clear()
    a=turtle.textinput(" ","kare dige ei nadari? Y or N: ")
    if a== "Y":
        kolesh()
    else:
        sys.exit()

darseee_morednazar = turtle.textinput(" ","edit ya didn ya ezafe krdn yek dars=esme dars ,didan kol list ya hazf yek dars =all : ")
if darseee_morednazar=="all":
        f=open("a11.json","r")
        x=f.read()
        turtle.penup()
        turtle.goto(-300,0)
        turtle.pendown()
        turtle.write(x,font=("Bold",13,'normal'))
        turtle.penup()
        turtle.goto(-100,0)
        turtle.pendown()
        q=turtle.textinput(" ","kodoom darsro mikhai hazf koni?(age nmikhay 'n' ro bzn)")
        if q in keys :
            del dicti[q]
            y=json.dumps(dicti)
            with open("a11.json","w") as esm_darsha:
                esm_darsha.write(y)
        if q not in keys:
            turtle.write("Hmchin darsi dar list vojood nadare")
        if q=="n":
            pass
        s=turtle.textinput("","car dige ei dari?=Y or N")
        while s=="Y":
            turtle.clear()
            kolesh()
        if s=="N" :
            sys.exit()

editYAdidn= turtle.textinput(" ","edit ya ezafe krdn dars =e , didn etelaat marboot be dars =d : ")

if editYAdidn == "e" or "d":
    if darseee_morednazar in keys:
        if editYAdidn =="e":
            t = turtle.textinput("etelaat marboot be dars ra vared konid : ","tarikh: ")
            r= turtle.textinput("etelaat marboot be dars ra vared konid : ","rooz: ")
            s= turtle.textinput("etelaat marboot be dars ra vared konid : ","saat: ")
            dicti[darseee_morednazar]=t+"-"+r+"-"+s
            y=json.dumps(dicti)
            with open("a11.json","w") as esm_darsha:
                esm_darsha.write(y)

        if editYAdidn == "d":
            turtle.write(dicti[darseee_morednazar],font=("Bold",15,'normal'))   

    else:
        while not editYAdidn in keys :
            turtle.write("moredi baraie in dars sabt nshde.")
            t =turtle.textinput("etelaat marboot be dars ra vared konid : ","tarikh: ")
            r=turtle.textinput("etelaat marboot be dars ra vared konid :","rooz: ")
            s=turtle.textinput("etelaat marboot be dars ra vared konid :","saat: ")
            dicti[darseee_morednazar]=t+"-"+r+"-"+s
            turtle.write("be list ezafe shod.")
            
            y=json.dumps(dicti)
            with open("a11.json","w") as esm_darsha:
                esm_darsha.write(y)
            break
break1=turtle.textinput(" ","baraye edame enter ro bznid")
turtle.clear()
a=turtle.textinput(" ","kare dige ei nadari? Y or N: ")
if a== "Y":
    kolesh()
else:
    sys.exit()

turtle.done()