RED='\u001b[31m'
RESET='\u001b[0m'
BLUE='\u001b[34m'
print(RED,"this will be in red ")
print("hellooooo")


def color_print(text: str, *effects: str)-> None:
    """   """
    effect_string="".join(effects)
    out_string="{0}{1}{2}".format(effect_string,text,RESET)
    print(out_string)



color_print("hello, red", RED)
color_print("hello, red bold", RED,bold)
#test that the color was reset

print("this should be in the default terminal color ")
color_print("hello, blue", BLUE)