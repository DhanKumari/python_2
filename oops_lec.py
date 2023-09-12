class student:
    

    def __init__(self,rollnum,name) :
        self.rollnum=rollnum
        self.name=name 


    def __init__(self,rollnum,age) :
        self.age=age


"""s1=student() #create objects in stack  memory
s1.print_hello()
print(s1.name)
s1.rollnum=2
print(s1.rollnum)"""

#parameterise constructor

s2=student(1,"kannu")
s2=student
print(s2.rollnum)
print(s2.name)
