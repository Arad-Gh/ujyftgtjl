import os
name = input("type a name ?")
x = name + ".txt"
all_files = os.listdir()
if x in all_files:
    for i in range(1, 100):
        x = name+str(i) + ".txt"
        all_files = os.listdir()
        if x in all_files:
            print("oh no !")
        else:
            print("done!")
            f = open(x, "a")
            f.close()
            break
else:
    f = open(x, "a")
    f.close()
    print("done !")
