from simple_deepcopy import my_deepcopy
import copy

original={
    "tim": ["buchalka", ["programmer", "Teacher"]],
    "J-P": ["Roberts", ["programmer", "Teacher"]],

}
copy_1= copy.deepcopy(original)  #perform deep copy
copy_2= my_deepcopy(original) #performs shallo copy 

original["tim"].append("Australia")
original["J-P"].append("UK")

original["tim"][1].append("cashier")
jp_list = original["J-P"]
jp_list[1].append("courier")

print(original)
print(copy_1)
print(copy_2)