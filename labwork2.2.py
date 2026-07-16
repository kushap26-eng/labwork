#1) maximum number from three numbers using nested if
# a = int(input("Enter a number a:"))
# b = int(input("Enter a number b:"))
# c = int(input("Enter a number c:"))

# if a > b :
#     if a > c:
#         print("Maximum number is:",a)
#     else:
#         print("Maximum number is:",c)
# else:
#     if b > c:
#         print("Maximum number is:",b)
#     else:
#         print("Maximum number is:",c)


#2) minimum number from three number using nested if
# a = int(input("Enter number a:"))
# b = int(input("Enter number b:"))
# c = int(input("Enter number c:"))
# if a < b:
#     if a < c:
#         print("MInimum number is:",a)
#     else:
#         print("Minimum number is:",c)
# else:
#     if b < c:
#         print("Minimum number is:",b)
#     else:
#         print("Minimum number is:",c)


#3) Maximum number from four numbers using nested if
# a = int(input("Enter number a:"))
# b = int(input("Enter number b:"))
# c = int(input("Enter number c:"))
# d = int(input("Enter number d:"))
# if a > b:
#     if a > c:
#         if a > d:
#             maximum = a
#         else:
#             maximum = d
#     else:
#         if c > d:
#             maximum = c
#         else:
#             maximum = d
# else:
#     if b > c:
#         if b > d:
#             maximum = b
#         else:
#             maximum = d
#     else:
#         if c > d:
#             maximum = c
#         else:
#             maximum = 4
# print("Maximum Number is:",maximum)


#4) Calculator using swithcase
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# operator = input("Enter operator(+, -, *, /):")

# match operator:
#     case "+":
#         print("Result = ",num1+num2)
#     case "-":
#         print("Result = ",num1-num2)
#     case "*":
#         print("Result = ",num1*num2)
#     case "/":
#         if num2 != 0:
#             print("Result = ",num1/num2)
#         else:
#             print("Divisible by zero is not allowed")
#     case _:
#         print("Invalid Operator")


#5) Menudriven Fastfood order system using match case
# print("FAST FOOD MENU")
# print("1. Sandwich")
# print("2. Pizza")
# print("3. Burger")
# choice = int(input("Enter your choice:"))
# match choice:
#     case 1:
#         print("Sandwich Menu")
#         print("1. Veg Sandwich")
#         print("2. Cheese Sandwich")
#         print("3. Mexican Sandwich")
#         sub = int(input("Enter your choice:"))
#         match sub:
#             case 1:
#                 print("You ordered Veg Sandwich")
#             case 2:
#                 print("You ordered Cheese Sandwich")
#             case 3:
#                 print("You ordered Mexican Sandwich")
#             case _:
#                 print("Invalid Choice")
#     case 2:
#         print("Pizza Menu")
#         print("1. Thin Crust Pizza")
#         print("2. Cheese Burst Pizza")
#         print("3. Fresh Dogh Pizza")
#         sub = int(input("Enter your choice:"))
#         match sub:
#             case 1:
#                 print("You ordered Thin Curst Pizza")
#             case 2:
#                 print("You ordered Cheese Burst Pizza")
#             case 3:
#                 print("You ordered Fresh Dogh Pizza")
#             case _:
#                 print("Invalid Choice")
#     case 3:
#         print("Burger Menu")
#         print("1. Veg Burger")
#         print("2. Cheese Burger")
#         print("3. Double Tikki Burger")
#         sub = int(input("Enter your choice:"))
#         match sub:
#             case 1:
#                 print("You ordered Beg Burger")
#             case 2:
#                 print("You ordered Cheese Burger")
#             case 3:
#                 print("You ordered Double Tikki Burger")
#             case _:
#                 print("Invalid Choice")
#     case _:
#         print("Invalid Main Menu Choice")


# menu driven telecom calling ststem using nested match case
# print("TELECOM CALLING SYSTEM")
# print("1. English")
# print("2. Hindi")
# print("3. Gijarati")

# language = int(input("Select Language:"))
# match language:
#     case 1:
#         print("\nEnglish Menu")


