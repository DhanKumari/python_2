
choice="-"  #initialise choice to somthing invalid
while choice!="0":
    #if choice in set("12345"):
    if choice in {"1","2","3","4","5"}:
        print("you chose {}".format(choice))
    else:#invalid choice 
        print("please choose from below ?")
        print("1:\tlearn" )
        print("2:\tlearn java" )
        print("3:\tlearn swimming " )
        print("4:\tplay" )
        print("5:\tsleep" )
        print("0:\texit" )

    choice=input()