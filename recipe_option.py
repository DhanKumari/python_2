

recipes_tuple ={
    "butter chicken " : [  #key : food name , value : list
        ("chicken",100),
        ("lemon",2),
        ("ginger",1),
        ("chilli",5),
    ],
}

recipes_dict={
    "butter chicken " : {  #key : food name , value : list
        "chicken":100,
        "lemon":2,
        "ginger":1,
        "chilli":5,
    },
  
}

#using tuples
for recipe,ingredients in recipes_tuple.items():
    print(f"ingredients for {recipe}")
    for ingredient, quantity in ingredients: #ingredients is a tuple
        print(ingredients, quantity, sep=', ')

print()

#using dictionary
for recipe, ingredients in recipes_dict.items():
    print(f"ingredients for {recipe}")
    for ingredient, quantity in ingredients.items(): #ingredients is a  dict
        print(ingredients, quantity, sep=', ')


