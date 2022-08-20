d1 = dict({"ram":20,"sita":25,"Divyanshu":7,"Ayush":30})
# print(d1,type(d1))
# d1["ram"] = 10
# print(d1["ram"])
# d1["Nishant"] = 100
# # print(d1["Ram"])
# d2 = {}#dict()
# print("Nishant" in d1)
# d1["ram"] = 200
# print(d1.get("nishant",0))
# d1[(1,2)] = "Hello"
# d1[10] = "Ramu"
# print(d1)

# x = d1.pop("ram")
# y = d1.popitem()
# print(x,y,d1)

dk = d1.keys()
d1["Ram"] = 100
print(dk,type(dk))
dv = d1.values()
print(dv,type(dv))

di = list(d1.items())
print(di,type(di))

for k,v in di:
    print(k,v)
    d1.pop(k)

