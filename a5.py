a = input(": ")
x=int(a[1])*10+int(a[2])*9+int(a[3])*8+int(a[4])*7+int(a[5])*6+int(a[6])*5+int(a[7])*4+int(a[8])*3+int(a[9])*2
w=x%11
if w<2 and int(a[10]) ==w or int(a[10])==11-w:
    print("Drste")
else :
    print("qlte")