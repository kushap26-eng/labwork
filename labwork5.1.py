# Object Oriented Program

#1) Create a class Person with attributes such as name and age.
# Write a method to display the details
# Create multiple objects and call the metod for each

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# person1 = Person("Kusha",23)
# person2 = Person("Isha",22)

# person1.display_details()
# person2.display_details()



#2) Develop a class Counter with an attribute count initialized to zero.
# Create methods to increment the count and display the value using self.

# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1

#     def display(self):
#         print(f"Count: {self.count}")

# counter = Counter()
# counter.increment()
# counter.increment()
# counter.increment()
# counter.display()


#3) Explain the behavior when self is omiited in a method definition using a small example.
#When self is omitted from a method definition in a Python class, the method becomes an ordinary function instead of an instance method. If you try to call it through an instance, Python automatically passes the instance as the first argument, resulting in a TypeError.
# class Example:
#     def greet():
#         print("Hello")

# object = Example()
# object.greet()


#4) Write a program to create a class Book with private attributes title and author.
# Add public methods to set and get these attributes

# class Book:
#     def __init__(self,title,author):
#         self.__title = title
#         self.__author = author

#     def set_title(self,title):
#         self.__title =title

#     def set_author(self,author):
#         self.__author = author

#     def get_title(self):
#         return self.__title

#     def get_author(Self):
#         return Self.__author

# book = Book("1984","George Orewell")
# print(book.get_title())
# print(book.get_author())


#5) Implement a class Account with a private attribute balance.
# Create methods to deposit and withdraw money.
# Add a method to display the balance.
# Ensure balance cannot be accessed directly.

# class Account:
#     def __init__(self,inital_balance = 0.0):
#         self.__balance = inital_balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Invalid Deposit amount.")

#     def withdraw(self,amount):
#         if amount > 0:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds or invalid amount.")

#     def display_balance(self):
#         print(f"Account Balance: ₹{self.__balance:.2f}")


# account = Account(100)
# account.deposit(50)
# account.withdraw(30)
# account.display_balance()


#6) Develop a program that usues getter and setter methods to validate the age of a person(e.g.,age must be greater than 0.)
# class ValidatedPerson:
#     def __init__(self,name,age):
#         self.nam = name
#         self.set_age(age)

#     def set_Age(self,age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Error: Age must be greater than 0.")
#             self.__age = 1

#     def get_age(Self):
#         return Self.__age

# person = ValidatedPerson("Kushangi",-5)


#7) Create a class Student with private attributes for ame and marks(of three subjects).
# Add a method to calculate and display the average.
# Add public methods to calculate and display the grade based on marks.

# class Student:
#     def __init__(self,name,marks_list):
#         self.__name = name
#         self.__marks = marks_list

#     def clculate_average(Self):
#         avg = sum(Self.__marks) / len(Self.__marks)
#         return avg

#     def display_average(Self):
#         print(f"{Self.__name}'s average Marks: {Self.clculate_average():.2f}")

#     def display_grade(Self):
#         avg = Self.clculate_average()
#         if avg >= 90:
#             grade = "A"
#         elif avg >= 75:
#             grade = "B"
#         elif avg >= 50:
#             grade = "C"
#         else:
#             grade = "F"
#         print(f"{Self.__name}'s Grade: {grade}")


# student = Student("Kushangi",[90,83,86])
# student.display_average()
# student.display_grade()