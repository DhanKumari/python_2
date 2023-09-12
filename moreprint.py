menu=[["apple,mango"],["egg","spam"],["egg","banana"],["apple","spam",],["tomato","egg","banana","apple"],]


for meal in menu:
    for item in meal:
        if item!="spam":
            print(item,end=", ")
    print()