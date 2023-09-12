from smart_fridge import pantry


#checking the item quantity present in fridge

chicken_quantity = pantry.setdefault("chicken",0)
print(f"chicken: {chicken_quantity}")


beans_quantity =pantry.setdefault("beans",0)  #setdefault returns the value n adds in the dict  with dafault value
print(f"beans: {beans_quantity}") 

ketchup_quantity =pantry.get("ketchup",0)  #get returns the default value 
print(f"ketchup: {ketchup_quantity}")

orange_quantity = pantry.setdefault("orange", "eight")  
print(f"orange: {orange_quantity}")



print()
print(" 'pantry' now contains..")

for key,value in sorted(pantry.items()):
    print(key,value)
