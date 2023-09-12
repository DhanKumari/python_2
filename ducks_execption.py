class Wing(object):
    
    def __init__(self, ratio):
        self.ratio = ratio
        
    def fly(self):
        if self.ratio>1:
            print("ee this is one ")
        elif self.ratio ==1:
            print("this is hard work")
        else:
            print("i think i'll just walk ")    
            
class Duck(object): 
    
    def __init__(self):  #constructor
        self._wing= Wing(1.8)
             
    def walk(self):
        print("waddle, waddle, waddle")
        
    def swim(self):
        print("come on it, the water's lovely")
        
    def quack(self):
        print("quack quack")
        
    def fly(self):
        self._wing.fly()  #composition 
        
class Panguin(object):
    def walk(self):
        print("waddle, waddle, i waddle too")
        
    def swim(self):
        print("come on it, its chilly")
        
    def quack(self):
        print("hahhaha") 
    
class Flock(object):
        def __init__(self):
            self.Flock=[]

        def add_duck(self,duck):
            self.flock.append(duck)

        def migrate(self):
            problem= None
            for duck in self.Flock:
                try:
                    duck.fly()
                except AttributeError as e:
                    print("one duck down")
                    problem=e
                    #raise
            if problem:
                raise problem
                duck.fly()

   
        
    
if __name__ =='__main__':
    donald=Duck()
    donald.fly()
    
"""     
def test_duck(duck):
    duck.walk() #calling a funtion 
    duck.swim()
    duck.quack()"""
    


    
"""

    percy = Panguin()
    test_duck(percy)    #panguin n duck both have same method swim , walk , quack."""
    