from smart_fridge import pantry,recipes
#print(pantry)
#print(recipes)
def add_shopping_item(data:dict, item:str, amount:int)->None:
    """add a tuple containing 'item' and 'amount' to the 'data' dict """
    """if item in data:
        data[item] += amount 
    else:
        data[item]= amount"""
    data[item] =data.setdefault(item,0) + amount


display_dict={}
for index, key in enumerate(recipes):
    display_dict[str(index +1)] = key 


shopping_list ={}
while True:
    print("------------------------------------------")
    print("please choose ur recipe ")
    print("__________________________________________")
    for key, value in display_dict.items():
        print(f"{key}-{value}")

    choice= input(": ")

    if choice =="0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"you have selected {selected_item} ")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)

        for food_item, required_quantity  in ingredients.items():
            quantity_in_pantry = pantry.get(food_item,0)
            if required_quantity<= quantity_in_pantry:
                print(f"\t{food_item} ok")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tyou need to buy {quantity_to_buy} of  {food_item} ")
                add_shopping_item(shopping_list,food_item,quantity_to_buy) #calling the function


for things in shopping_list.items():
    print(things)

   
