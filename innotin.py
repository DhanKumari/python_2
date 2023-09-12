parrot="norwegian blue"

letter=input("enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))


activity=input("what would u like to do tody ?")

if "cinema" not in activity.casefold():
    print("but i would like to go to cinema")
