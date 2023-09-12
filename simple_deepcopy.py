from smart_fridge import recipes

def my_deepcopy(d:dict)-> dict:

    """copy a dictionary , creating copies of the  'list' or 'dict' values """
    new_dict={}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict



recipes_copy= my_deepcopy(recipes)  #calling a function 
recipes_copy["butter chicken"]["ginger"]= 300
print(recipes_copy["butter chicken"]["ginger"])
print(recipes["butter chicken"]["ginger"])