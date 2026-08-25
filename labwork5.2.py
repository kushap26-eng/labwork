# OOP

#1) Write a program that creates multiple objects of a class and deletes them using the del keyword.
# Observe te behavior(using the destructor)

# class Item:
#     def __init__(self,name):
#         self.name = name
#         print(f"Object '{self.name}' created.")

#     def __del__(self):
#         print(f"Destructor called: Object '{self.name}' deleted.")

# obj1 = Item("A")
# obj2 = Item("B")
# obj3 = Item("C")

# print("Deleting obj1 explicitly:")
# del obj1

# print("All Objects deleted.")



#2) Create a class Animal with a constructor that initializes the name attribute.
# Add a method to display the name of the animal

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def display_name(self):
#         print(f"The animal's name is: {self.name}")

# lion = Animal("Simba")
# lion.display_name()


#3) Write a program to demonstrate a parameterized constructor in the class Rectangle.
# Intialize the length and width using the constructor and calculate the area.

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

# rectangle = Rectangle(10,5)
# area = rectangle.calculate_area()
# print(f"Rectangle Area: {area}")


#4) Create a class Employee with a default constuctor to initialize attributes and a 
# destrctor to display a farewell message when the object is deleted.

# class Employee:
#     def __init__(self):
#         self.name = "Guest User"
#         self.role = "unassigned"
#         print(f"Employee profile created for {self.name}")

#     def __del__(self):
#         print(f"Farewell messag: Employee '{self.name}' session ended.")

# emp = Employee()
# del emp


#5) Create a class student with appropriate attributes and methods,along with a constructor.
class Student:
    def __init__(self,student_id,name,grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display_profile(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade}")

    def update_grade(self,new_grade):
        self.grade = new_grade
        print(f"Grade updated for {self.name} to {self.grade}")

student1 = Student("s101", "Kusha","A")
student1.display_profile()
student1.update_grade("A+")
student1.display_profile()


