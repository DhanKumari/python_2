class kettle(object):
    
    power_source="electricity"
    
    def __init__(self, make, price): #method
        self.make = make
        self.price = price
        self.on=False
        
    def switch_on(self):   #method 2 
        self.on=True
        
        
        
kenwood= kettle("kenwood", 8.99) #object
print(kenwood.make)
print(kenwood.price)

kenwood.price=22.3
print(kenwood.price)

hamilton = kettle("hamilton",33.3) #object 2 
print(hamilton.make)
print(hamilton.price)


print("models: {}={}, {}={}".format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))

print("models: {0.make} ={0.price}, {1.make} = {1.price}".format(kenwood,hamilton))

print(hamilton.on)
hamilton.switch_on() #calling method
print(hamilton.on)


kettle.switch_on(kenwood) #calling a method 
print(kenwood.on)

print("*"*8)
print(kettle.power_source)
print(hamilton.power_source)
print(kettle.__dict__)
print(hamilton.__dict__)