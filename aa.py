import os
import random
name = input("name :")
b = os.listdir()
c = name +".txt"
n = 0 
while n< 999 :
    n = n-1
    break
x = name  + str(n) + ".txt"
if c in b :
    o = open(x , "a")
    o.close()
else :
    o = open(c , "a")
    o.close()