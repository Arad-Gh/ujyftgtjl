a= "I'm student"
#a=input("english : ")
b= a.split(" ")
dic = {
    "student":"daneshamoz",
    "hello":"salam",
    "I'm" : "mn"
}
x=len(b)
w=dic.keys()
z=""
for i in b:
    z = z+dic[i]
