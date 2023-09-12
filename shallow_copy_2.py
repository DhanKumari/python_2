lion_list=["scary","big","cat"]
elephant_list= ["big","grey","wrinkled"]
teddy_list=["cuddely","stuffed"]


animals = {
    "lion": lion_list,
    "elephant":elephant_list,
    "teddy": teddy_list,

}

things = animals.copy()
#animals["teddy"]= "toy"
print(things["teddy"])

print(animals["teddy"])

print()

#things["teddy"].append("toy")
teddy_list.append("toy")
print(things["teddy"])
print(animals["teddy"])