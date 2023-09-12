import random
ans=random.randint(1,50)

#print(ans)
guess=0
print("guess a no.")


while guess !=ans:
    guess=int(input())
    if guess== ans:
            print("correct")
            break
    else:
        if guess <ans:
            print("guess higher ")
        else:
             print("guess lowwer ")

