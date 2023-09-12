def fizz_buzz(num:int)->str:
   # fizz % by 3
     #buzz is % 5 
     # fizz buzz is divisible by both 3 and 5 
    if num % 15 ==0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return"buzz"
    else: 
        return str(num)
    

"""  
for i in range(1,101):
    print(fizz_buzz(i))
   """

input("play fizz buzz.  press ENTER to start")
print()

next_num=0
while next_num<99:
    next_num+=1
    print(fizz_buzz(next_num))
    next_num+=1
    correct_ans=fizz_buzz(next_num)
    #player_ans= input("your go: ")
    player_ans= correct_ans
    if player_ans!= correct_ans:
        print("you lose the correct ans was {}".format(correct_ans))
        break

else:
    print("well done, you reached {}".format(next_num))


