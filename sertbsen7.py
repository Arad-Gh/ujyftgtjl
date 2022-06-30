import json
a= {
    "riazi":"shnbe-12:30",
    "fizik":"yekshnbe-11:00",
    "shimi":"doshnbe-10:00"
}
b=json.dumps(a)
with open("a10.json","w") as myfile:
    myfile.write(b)