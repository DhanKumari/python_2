travel_mode={"1":"car","2":"plane"}

items={
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "razzor",
    "shirts",
}
restricted_items ={
    "catapult",
    "fuel",
    "knife",
    "shampoo",
    
    }

print("please choose your mode of travel: ")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    
    
mode = "-"
while mode not in travel_mode:
    mode = input("> ")
    
if mode == "2":
    #for restricted_item in restricted_items:
      #  items.discard(restricted_item)
    items -= restricted_items  # items r removed in one single line then using the two line code  

print("you need to pack: ")
for item in sorted(items):
    print(item)

    
    