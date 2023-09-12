v={"1":"blue",
   "hi": "orange",
   "hey":"purple",
   "2":"purple",
   "5":"purple",


}
#print(v[1])
a=v.get("hi")
#print(a)
#for key in v:
 #   print(key,v[key],sep=", ")

v["hey"]="black"     # adding new value 
v["1"]="pink"         #change value
del v["hey"]        #delete
v.pop("hi")         #delete

for key,value in v.items():
    print(key,value, sep=",")