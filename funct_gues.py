
import random

def get_integer(prompt):
     
     while True:
          temp=input(prompt)
          if temp.isnumeric(): #that input is numeric 
               return int(temp)
          #else:
          print("{} is not a valid no.".format(temp))



ans=random.randint(1,50)

#print(ans)
guess=0
print("guess a no.")


while guess !=ans:
    guess=get_integer(": ")

    if guess==0:
         break
    if guess== ans:
            print("correct")
            break
    else:
        if guess <ans:
            print("guess higher ")
        else:
             print("guess lower ")

