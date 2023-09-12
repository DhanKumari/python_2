#multilevel
class grandparent:
    def  __init__ (self,name,age):
        self.name=name
        self.age=age
        
class parent(grandparent):
    def __init__ (self,id):
        super().__init__(name,age)
        self.id=id
        
class child(parent):
    def __init__(self,name,age,id, color):
        super().__init__(self,name , age ,id)
        self.color=color
        
        
s1= studdent("kannu",23,123,"blue")  #check the error 
print(s1.color)
    