class Student:
    def __init__(self, name, major, gpa, is_on_probation): #these are the requirements of our class
        self.name = name #these are our conditions or objects
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        
    def on_honor_roll(self): #this is a function within a class as an extra condition that checks honor roll on the object gpa also known as a object function
        if self.gpa >= 3.5:
            return True
        else:
            return False

