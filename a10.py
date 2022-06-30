import json
a= {
    "st1":"111",
    "st2":"222"
}
b=json.dumps(a)
with open("a10.json","w") as myfile :
    myfile.write(b)