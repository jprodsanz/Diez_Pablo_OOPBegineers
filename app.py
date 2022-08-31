#object Oriented Programmin in Python
# objects are an instance of a specifc class
# classes define the way in which that object interacts with other elements in our program

# def hello():
#     print('hello')
# x = 1
# print(type(hello))

# string = 'hello'
# #this is a method
# print(string.upper())

# What is a method?
# A method is a function that goes inside a class, boom! 

class Dog: 

#special method def __init__(self):
    def __init__(self,name, age):
        #attribute alert below
        self.name = name
        self.age = age
        print(name)
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age
        pass

    
    # def add_one(self,x):
    #     return x + 1
    
    # def bark(self):
    #     print('bark')

# d  in this case is a new instance of the class
d = Dog('Max',32)
d.set_age(23)
print(d.get_age())

# d2 = Dog('Pumba',32)
# d.bark()
# print(d.add_one(5))  
# print(type(d))
