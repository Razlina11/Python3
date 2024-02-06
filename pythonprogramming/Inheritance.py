class parent:
    'This is a demo class'
    _age=30  #class variable
    def __init__(self,name): #current class dealing,magic method
        self.name=name
        print('parent object created')
    def sayhello(self):
        print("The parent name is {self.name} and the age is {parent.age}")        
class child(parent):
    def __init__(chill,age):
        chill.age=age
        print("Child object is created")
        parent.__init__(chill,'Ashish')
    def childname(chill):
        print(f'Name of the parent is {chill.name} and the age is {chill.age}')
    
obj=parent('comic')
objc=child(7)
              
