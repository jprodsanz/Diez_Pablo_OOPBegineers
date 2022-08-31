class Person:
    number_of_people = 0
    GRAVITY = -9.8
    
    def __init__(self,name):
        self.name = name
        Person.add_person()

    # this method acts ont the class itself as opposed to objects
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people())


# Person_number_of_people = 8
# print(p2.number_of_people)
# print(p2.number_of_people)