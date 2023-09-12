panagram="the quick brown fox jumps over the lazy dog "
words=panagram.split()  #since we didnt mention hwere to split ittakes space 
print(words)


n=["1","2","3","4","5","6",]
values=" ".join(n)
print(values)

val_list=values.split()
print(val_list)
print("_"*10)
# use for loop to produce a list of int, rather than strings 
#sol 1
"""for i in range(len(val_list)):
    val_list[i]=int(val_list[i])
print(val_list)
"""
#sol 2
int_val=[]
for values in val_list:
   int_val.append(int(values))
print(int_val)