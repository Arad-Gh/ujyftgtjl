import os
sign = input("Do you have an account? ")
if sign == "yes" or "y" :
    name3 = input("Username: ")
    email3 = input("email: ")
    password3 = input("password: ")
    user1 = "name:" + name3 + " password:" + password3 + " email:" + email3
    a=os.listdir()
    x =name3 + ".txt"
    if x in a :
        q = open(x , "r")
        if user1 == q:
            print("Welcome to your account ", name3, ("!"))
else :
    name2 = input("choose a name: ")
    a = os.listdir()
    x = name2 + ".txt"
    if  x in a :
        print("You can't use this stopname")
    else :
        email = input("email: ")
        password = input("choose a pssword: ")
        email = input("email: ")
        password = input("choose a pssword: ")
        password2 = input("repeat your password: ")
        if password2 == password:
            user = "name:" + name2 + " password:" + password2 + " email:" + email
            f = open(name2 + ".txt", "a")
            f.write(user)
            f.close()
            print("Your account is ready !")
            print("Press start again. ")
        else :
            print("eshtb nvshti")