# Inheritance Labwork

#1) Create a program to demonstrate Single Inheritance where a class Parent has a method 
# display(),and a child class Child inherits and calls this method.

# class Parent:
#     def display(self):
#         print("This is a methodfrom the parent class.")

# class Child(Parent):
#     def child_method(self):
#         print("This is a method from the Child class.")

# object = Child()
# object.display()
# object.child_method()


#2) Implement a program to demonstrate Multiple Inheritance using classes Teacher and administrator inherited by a class Headmaster.

# class Teacher:
#     def teach(self):
#         print("Teaching students.")

# class Administrator:
#     def manage(self):
#         print("Managing school operations.")

# class Headmaster(Teacher,Administrator):
#     def lead(Self):
#         print("Leading the school.")


# head_master = Headmaster()
# head_master.teach()
# head_master.manage()
# head_master.lead()


#3) Write a program to demonstrate Multilevel Inheritance using a class hierarchy:
# Grandparent -> Parent -> Child.
# Each class should have a method to display its role.

# class Grandparent:
#     def display_grandparent(self):
#         print("Role: Grandparent")

# class Parent(Grandparent):
#     def display_parent(self):
#         print("Role: Parent")

# class Child(Parent):
#     def display_child(self):
#         print("Role: Child")

# kid = Child()
# kid.display_grandparent()
# kid.display_parent()
# kid.display_child()


#4) Create a program to demonstrate Hierarchical Inheritance where a base class Animal is inherited by two subclass Dog
# and cat,each having their specific methods.

# class Animal:
#     def eat(self):
#         print("This animal eats food.")

# class Dog(Animal):
#     def bark(self):
#         print("The dog barks: Woof!")

# class Cat(Animal):
#     def meow(self):
#         print("The cat meows: Meow!")

# dog = Dog()
# cat = Cat()

# dog.eat()
# dog.bark()

# cat.eat()
# cat.meow()


#5) Develop a program to demonstrate Hybrid Inheritance by combinning Multilevel and 
# Multiple inheritance. Show how the super() function helps resolve ambiguity.

# class A:
#     def show(self):
#         print("Method in class A")

# class B:
#     def show(self):
#         print("Method in class B")
#         super().show()

# class C(A):
#     def show(self):
#         print("Method in class C")
#         super().show()

# class D(B,C):
#     def show(self):
#         print("Method in class D")
#         super().show()


# obj = D()
# obj.show()


#6) Write a program to demonstrate the use of the type() function to retrive the type of a variable or object.

# name = "Kusha"
# age = 22
# pi_value = 3.14
# is_student = True

# class Student:
#     pass

# student_obj = Student()

# print(f"Type of 'n': {type(name)}")
# print(f"Type of 'age': {type(age)}")
# print(f"Type of 'pi_value': {type(pi_value)}")
# print(f"Type of 'is_student': {type(is_student)}")
# print(f"Type of 'student_obj': {type(student_obj)}")



#7) Write a program to list all the attributes and methods of a class using the dir() function.

# class Car:
#     def __init__(self,brand):
#         self.brand = brand

#     def drive(self):
#         print("The car is moving")

# car_directory = dir(Car)

# print("All items in Car Class: ")
# print(car_directory)

# user_items = [item for item in car_directory if not item.startswith("__")]
# print(user_items)


#8) Develop a program to check if an instance of a particular class using the instance() function.

# class Vehicle:
#     pass

# class Bike(Vehicle):
#     pass

# my_bike = Bike()
# my_string = "Hello"

# print("Is 'my_bike' an instance of Bike?", isinstance(my_bike,Bike))
# print("Is 'my_bike' an instance of Vehicle(Parent)?",isinstance(my_bike,Vehicle))
# print("Is 'my_string' an instance of Vehicle?",isinstance(my_string,Vehicle))
# print("Is 'my_string' an instance of str?",isinstance(my_string,str))



#9) Write a program to retrive the documentation string of a class or function using the helip() function.

# def calculate_area(radius):
#     '''
#     Calculates the area of  circle.
#     Parameters:
#           radius(float): The radius of the circle.
#     Returns:
#           float: The calculated area.
#     '''
#     return 3.14*(radius**2)

# help(calculate_area)