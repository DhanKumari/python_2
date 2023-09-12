small_ints = set(range(20))
print(small_ints)
#small_ints.clear()
#print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)