shopping=["milkk","pasta","bread","spam","banana"]

item_to_find="spam"
found_at=None


#for i in range(6):
if item_to_find in shopping:
    found_at=shopping.index(item_to_find)

if found_at is not None:
    print(" item found at position {}".format(found_at))
else:
    print("{} item not found".format(item_to_find))


