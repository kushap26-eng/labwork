#1) Write a program to demonstrate polymorphism in functions by defining a 
# function add() that can take either two integer or two strings and perform addition or concatention.

# def add(a,b):
#     return a + b

# print(add(5,10))

# print(add("Hello","World"))


#2) Implement a program to demonstrate polymorphism in class inheritance.
# Create a base class Shape with a method area() and derive classes Circle and 
# Rectangle overriding the area() for their specific calculations.

# class Shape:
#     def area(Self):
#         return 0

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(Self):
#         return 3.14* Self.radius * Self.radius

# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(Self):
#         return Self.width * Self.height

# shapes = [Circle(5),Rectangle(4,6)]

# for shape in shapes:
#     print("Area: ",shape.area())


#3) write a program to demonstrate polymorphism with a built-in function len()
# by applying it to a string,list,and dictionary.

# my_string = "Python"
# print(len(my_string))
# my_list = [10,20,30,40]
# print(len(my_list))
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(len(my_dict))



#4) Create a program using polymorphism where an interface Transport has a method travel()
# Implement it differently in classes Train and Plane.

# class Transport:
#     def travel(self):
#         return "Travelling by generic transport..."

# class Train(Transport):
#     def travel(self):
#         return "Train: Traveling by tracks"

# class Plane(Transport):
#     def travel(self):
#         return "Plane: Traveling throgh the skies"

# vehicles = [Train(),Plane()]

# for vehicle in vehicles:
#     print(vehicle.travel())


#5) Write a program to demonstrate method overloading by creating a class Calculator with
# a method multiply() that works for two or three arguments.
# Use default arguments or variable length arguments.

# class Calculator:
#     def multiply(self,a,b,c=1):
#         return a * b * c

# calc = Calculator()
# print(calc.multiply(4,5))
# print(calc.multiply(2,3,4))


#6) Implement a program to demonstrate method ovrriding where a class Animal
# has a method speak(),and subclasses Dog and Cat override it with their respective sounds.

# class Animal:
#     def speak(self):
#         return "Some animal Sound"

# class Dog(Animal):
#     def speak(self):
#         return "Dog: Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Cat: Mepow"

# pets = [Dog(),Cat()]
# for pet in pets:
#     print(pet.speak())


#7) Create a program  to show method overloading using the same method name area()
#but performing different operations for a circle and rectangle by using @staticmethod
# or @classmethod.

# class Shape_Calculation:
#     @staticmethod
#     def area_circle(radius):
#         return 3.14 * radius * radius

#     @classmethod
#     def area_ractangle(cls,width,height):
#         return width * height

# print("Circle area: ",Shape_Calculation.area_circle(5))
# print("Rectangle area: ",Shape_Calculation.area_ractangle(4,9))


#8) Write a program where a parent class vehicle has a method start()
# Demonstrate method overriding in the child classes Bike and Car with
# different logic.

# class Vehicle:
#     def start(self):
#         return "Vehicle system initializing..."

# class Bike(Vehicle):
#     def start(self):
#         return "Bike: Kick starting the ignition and revving the engine"

# class Car(Vehicle):
#     def start(self):
#         return "Car: Pushing the start button and turning on AC."

# fleet = [Bike(),Car()]
# for vehicle in fleet:
#     print(vehicle.start())


#9) Develop a program to showcase method overloading by implementing a class 
# Printer with a print() method that prints either a string,an integer,or both
# based on the arguments provided.

# class Printer:
#     def print(self,*args):
#         if len(args) == 0:
#             print("No arguments provided.")

#         elif len(args) == 1:
#             item = args[0]
#             if isinstance(item,int):
#                 print(f"Integer: {item}")
#             else:
#                 print(f"String: {item}")

#         elif len(args) == 2:
#             print(f"Both: String = {args[0]}, Integer = {args[1]}")

#         else:
#             print("Too many arguments provided.")

# printer = Printer()
# printer.print()
# printer.print("Hello")
# printer.print(42)
# printer.print("Python",100)



#10) Write a program to demonstrate the use of issubclass () by creating classes
# Person and Student(derived from Person).
# Check if Student is a subclass of Person and print the result.

# class Person:
#     pass

# class Student(Person):
#     pass 

# is_derived = issubclass(Student,Person)
# print(f"Is Student a subclass of Person? {is_derived}")


#11) Implement a program where super() is used in a class Manager to call
# the constructor of its parent class Employee.
# The parent class should have attributes like name and salary.

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         print(f"Employee created Name: {self.name},Salary: ₹{self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary,department):
#             super().__init__(name,salary)
#             self.department = department
#             print(f"Mnager constructor called for department: {self.department}")

# mgr = Manager("Kushangi",95000,"IT Operations")



#12) Write a program to demonstrate issubclass() in a multilevel inheritance
# hierarchy where Grandparent -> Parent -> Child
# Use the function to check subclass relationships.

# class Grandparent:
#     pass
# class Parent(Grandparent):
#     pass
# class Child(Parent):
#     pass

# is_child_of_parent = issubclass(Child,Parent)
# is_child_of_grandparent = issubclass(Child,Grandparent)
# is_parent_of_grandparent = issubclass(Parent,Grandparent)

# print(f"Is Child a subclass of Parent? {is_child_of_parent}")
# print(f"Is Child a subclass of Grandparent? {is_child_of_grandparent}")
# print(f"Is Parent a subclass of Grandparent? {is_parent_of_grandparent}")


#13) Create a program to demonstrate super() in a method.
# Define a class Base with a method display().
# Override the method in a derived class Derived and call the base class's 
# method using super().

# class Base:
#     def display(self):
#         print("This is the display() method from the base class.")

# class Derived(Base):
#     def display(self):
#         super().display()
#         print("This is the overridden display() method in Derived class.")

# obj = Derived()
# obj.display()


#14) Develop a program where a class Amin inherits from User.
# use super() to initialize the attributes of the User class in the Admin constructor.

# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
#         print(f"User profile created for: {self.username}")

# class Admin(User):
#     def __init__(self, username, email,access_leevl):
#         super().__init__(username,email)
#         self.access_level = access_leevl
#         print(f"Admin level granted: {self.access_level}")

# admin_user = Admin("root_user","admin@company.com","SuperAdmin")