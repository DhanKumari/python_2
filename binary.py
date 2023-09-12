#hi lo game 
low=1
high=1000

print("choose a no. btw {} and {}".format(low,high))
input("press enter to start")

guesses=1
while True:
    print("guessing in the range {}and{}",format(low, high))
    guess=low +(high-low)//2 #mid pt
    high_low=input("my guess is {},should i guess higher or lower "
                   "enter h or ,l or c if my ans is correct ".format(guess)).casefold()
    
    if high_low=="h":
        low=guess+1
#guess higher. the lower range of the low no. becomes one greater thsn the guess
    elif high_low=="l":
        high=guess-1
        #guess lower . 
    elif high_low=="c":
        print("i got it in {} guess".format(guesses))
        break
    else:
        print("please enter h,l or c")

    guesses=guesses+1
