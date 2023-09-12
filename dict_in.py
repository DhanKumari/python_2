available_parts ={"1":"blue",
   "2": "orange",
   "3":"purple",
   "4":"pink",
   "5":"black",
   "6":"white",

}

current_choice = None
computer_parts={}  #empty dict
while current_choice !="0":
    if current_choice in available_parts: #it checks the key 
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
        #its already in so remove it 
            print(f"removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            
            print(f"adding {chosen_part}") #.format
            computer_parts[current_choice] = chosen_part
        print(f"your dictionary now contains: {computer_parts}")
    else:
        print("add options from the list")
        for key, value in available_parts.items():
            print(f"{key}:{value}")
        print("0: to finish")

    current_choice = input(">")
