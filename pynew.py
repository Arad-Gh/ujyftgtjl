'''a = "    444456567546465     "
b = len(a)  shomordn hoorof
print(b)
b = a.strip() hazf space ha'''

#--------------------------------
import os
sign = input("Do you have an account? ")
if sign == "yes" :
    name1 = input("Username: ")
    password = input("password: ")
    print("Welcome to your account ", name1, ("!"))
else :
    name2 = input("choose a name: ")
    a = os.listdir()
    x = name2 + ".txt"
    if  x in a :
        print("You can't use this name")
    email = input("email: ")
    password = input("choose a pssword: ")
    email = input("email: ")
    password = input("choose a pssword: ")
    password2 = input("repeat your password: ")
    if password2 == password:
        print("Your account is ready !")
    else :
        print("eshtb nvshti")
        password = input("choose a pssword: ")
        password2 = input("repeat your password: ")
    user = "name: " + name2 + " password: " + password2 + " email: " + email
    f = open(name2 + ".txt", "a")
    f.write(user)
    f.close()
    name3 = input("Username: ")
    password1 = input("password : ")
    if password1 != password or name3 != name2 :
        print("Your username or password is wrong")
    if password1 == password and name3==name2:
        print("Welcome to your account ", name2, ("!"))
