ava_exit=["n","s","w","e"]
chosen_exit=""
while chosen_exit not in ava_exit:
    chosen_exit=input("enter a direction")
    if chosen_exit.casefold()=="quite":
        print("game over")
        break

print("glad u  got ur direction ")
