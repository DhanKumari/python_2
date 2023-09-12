name=input("enter your name ")
age=int(input("how old are u {0} ".format(name)))
print( age)
#sent=input("{0} are u {1} years old ?".format(name, age))

if age >= 18:
    print("you are old enugh to vote ")
elif age==100:
    print("century ")
else:
    print(" ue age doesn't match the voting conditions ")

