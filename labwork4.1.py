# Function Array and Sorting
#1) Program using at least five built in function
# numbers = [10,5,8,20,15]
# print("List: ",numbers)
# print("Length: ",len(numbers))
# print("Maximum: ",max(numbers))
# print("Sum: ",sum(numbers))
# print("Sorted List: ",sorted(numbers))
# print("Type; ",type(numbers))


#2) UDF to calculate factorial
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# num = int(input("Enter a number: "))
# print("Factorial: ",factorial(num))



#3) UDF to return square of each integer using list comprehension
# def square_list(numbers):
#     return [num ** 2 for num in numbers]
# nums = [1,2,3,4,5]
# print("Original List: ",nums)
# print("Squared List: ",square_list(nums))


#4) UDF to return frequency of each character
# def frequency(text):
#     dict = {} 
#     for ch in text:
#         if ch in dict:
#             dict[ch] += 1
#         else:
#             dict[ch] = 1
#     return dict
# string = input("Enter a String: ")
# print(frequency(string))



#5) Pass a UDF as an argument to calculate cube
# def cube(numbers):
#     return [num ** 3 for num in numbers]
# num = [1,2,3,4,5]
# print("Original Numbers: ",num)
# print("Cube: ",cube(num))


#6) Function accepting arbitary function
# def sum_product(*args):
#     total = sum(args)
#     product = 1
#     for num in args:
#         product *= num
#     return total,product
# sum,product =sum_product(2,3,4,5)
# print("Sum: ",sum)
# print("Product: ",product)


#7) Print Student names using *args
# def student_names(*args):
#     if len(args) == 0:
#         print("Student List is empty.")
#     else:
#         print("Student names: ")
#         for name in args:
#             print(name)

# student_names("Kushangi", "Vishwa", "Heer")
# student_names()



#8) Filter strings from argument
# def filter_values(*args):
#     strings = tuple(item for item in args if isinstance(item,str))
#     numbers = tuple(item for item in args if isinstance(item,(int,float)))
#     return strings,numbers
# strings,numbers = filter_values("Python",10,"AI",5,3.2)
# print("Strings: ",strings)
# print("Numbers: ",numbers)


#9) Write a function that accepts **kwargs to print details of a person.
# def person(**kwargs):
#     print("Name: ",kwargs["name"])
#     print("Age: ",kwargs["age"])
#     print("City: ",kwargs["city"])
# person(name="Kushangi",age=21,city="Ahmedabad")



#10) Product details using **kwargs
# def product_details(**kwargs):
#     total_cost = kwargs["price"] * kwargs["quantity"]
#     return f"Product: {kwargs['name']},Total Cost: ₹{total_cost}"
# print(
#     product_details(
#         name = "Laptop",
#         price = 50000,
#         quantity = 2
#     )
# )



#11) Employee atributes using **kwargs
# def employee_info(**kwsargs):
#     if "name" in kwsargs and "department" in kwsargs and "salary" in kwsargs:
#         print("Employee Details")
#         print("Name:",kwsargs["name"])
#         print("Department:",kwsargs["department"])
#         print("Salary:",kwsargs["salary"]
#     else:
#         print("Required fields are missing")
# employee_info(name="Kushangi",department="Research",salary=80000)



#12) Create a function that calculates the area of a rectangle
# Add a__doc__ string to describe the function's purpose ,parameters and return type
# write a code to print the__doc__string.

# def rectangle_area(length,width):
#     '''
#     Calulate the area of rectangle
#     Parameters:
#     length(float): length of rectangle
#     width(float): width of rectangle

#     Returns:
#     float: Area of rectanagle.
#     '''
#     return length * width
# area = rectangle_area(10,5)
# print("Area: ",area)
# print("\nDoc String:")
# print(rectangle_area.__doc__)



#13) Develop a program that use a UDF to return the FIbonnacci sequence up to a given number.
# Include a detailed __doc__string explaining the function's working,input,and output

# def fibonacci(n):
#     '''
#     This function returns the fibonacci sequence up to given number

#     Input:
#     n - Maximum number up to which the fibonacci sequence is generated

#     Output:
#     Returns a list containing the fibonaci numbers up to n.
#     '''
#     a = 0
#     b = 1
#     fib = []
#     while a <= n:
#         fib.append(a)
#         a,b=b,a+b
#     return fib
# num = int(input("Enter a number: "))
# print("Fibonacci Sequence: ",fibonacci(num))
# print("\nDoc String:")
# print(fibonacci.__doc__)