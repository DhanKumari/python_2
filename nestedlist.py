menu=[["apple,mango"],["egg","spam"],["egg","banana"],["apple","spam",],["tomato","egg","banana","apple"],]

"""for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        meal.remove("spam")
        print(meal)
       """

for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index]=="spam":
            del meal[index]
    print(",".join(meal) )

"""for meal in menu:
    for item in meal:
        if item!="spam":
            print(item)
    print()
        """
