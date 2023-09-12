
choice="-"
while True:
    if choice=="0":
        break
    elif choice in "12345":
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
