farm_animals={'cow','sheep','hen','goat','horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)
    
print()
print("indexing a sequence")
animals_list=['cow','sheep','hen','goat','horse']
goat = animals_list[3] 
print(goat)

print()
more_animals = {'sheep','goat','cow','horse','hen'}
if more_animals==farm_animals:
    print("set is equal")
else:
    print("set iis not equal")