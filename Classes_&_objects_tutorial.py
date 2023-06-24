from Student import Student #this imports our class

student1 = Student("Jonny Depp", "Computer Science", 3.1, False)
student2 = Student("Hanna", "Commerce", 2.4, True)
print(student2.name)#variable.object_name
print(student1.is_on_honor_roll())#object function
print(student2.is_on_honor_roll())
