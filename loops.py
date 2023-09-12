number= "9,223;938,390 398,309;398"

seperators =""
value=""

for char in number:
    if not char.isnumeric():
        seperators+=char

    else :
        value=value+char
        

print(seperators)
print(value)



