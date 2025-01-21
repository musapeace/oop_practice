class student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
# defining method 
    def student_class(self):
        return F"the student name is {self.name} and he is {self.age} years old"

# creating student object 
student1 = student("Arabee", 26)
student2 = student("Muhammad", 25)

print(f"{student1.student_class()}")
print(f"{student2.student_class()}")           