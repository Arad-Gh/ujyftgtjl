#import requests
from PIL import Image
#r=requests.get("https://www.handicappedpets.com/wp-content/uploads/2019/07/Hope-duck-ww.jpg")
#file = open("CrippleDuck.png" , "wb")
#file.write(r.content)
#file.close()
x=Image.open("CrippleDuck.png")
x.show()