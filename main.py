from enemy import Enemy,Troll,Vampyre, VampyreKing

dracula = VampyreKing("dracula")
print(dracula)
dracula.take_damage(12) #12 divide 4 = 3
print(dracula)

"""
random_monster = Enemy("basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll=Troll("kannu") #since we didnt pass anything there it defaullt takes enemy values 
print("ugly troll - {}".format(ugly_troll))

another_troll=Troll("ohh")
print("another troll - {}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

brother=Troll("ugg") #lives is default 1 as given in enemy
print(brother)

ugly_troll.grunt()

another_troll.grunt()

brother.grunt()

vamp = Vampyre("arjun")
vamp.take_damage(5)
print(vamp)

print("_"*10)
another_troll.take_damage(18)
print(another_troll)
print("_"*10)

###while vamp.alive:
        #vamp.take_damage(1)
        #print(vamp)
        
vamp._lives=0
vamp._hit_points=1
print(vamp)"""