shopping=["milkk","pasta","bread","spam","banana"]

item_to_find="spam"
found_at=None


#for i in range(6):
for index in range(len(shopping)):
    if shopping[index]==item_to_find:
        found_at=index
        break

print("item found at position {}".format(found_at))