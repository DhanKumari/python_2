import copy 



animals = {
    "lion": ["scary","big","cat"],
    "elephant":["big","grey","wrinkled"],
    "teddy": ["cuddely","stuffed"],

}
#perform shallo copy
#things = animals.copy()
#animals["teddy"]= "toy"


#perform deep copy
#things = copy.deepcopy(animals)

print(id(things["teddy"]),things["teddy"])
print(id(animals["teddy"]),animals["teddy"])

print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])