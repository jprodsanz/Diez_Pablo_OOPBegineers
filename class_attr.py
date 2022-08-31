class Person:
    # this below is a called a constant
    number_of_people = 0
    
    def __init__(self,name):
        self.name = name

p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)

# Person_number_of_people = 8
# print(p2.number_of_people)
# print(p2.number_of_people)