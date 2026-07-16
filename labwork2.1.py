# 1) check whether number is even or odd
# n = int(input("Enter a number:"))
# if n % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is odd")


#2) Catogarize age groups
# age = int(input("Enter a number:"))
# if age >= 0:
#     if age <= 12:
#         print("Child")
#     else:
#         if age <= 19:
#             print("Teenager")
#         else:
#             if age <= 59:
#                 print("Adult")
#             else:
#                 print("Senior")
# else:
#     print("Invalid Age")


#3) Largest number among three number using if-elif-else
# a = int(input("Enter number a:"))
# b = int(input("Enter number b:"))
# c = int(input("Enter number c:"))
# if a >= b and a >= c:
#     print("Largest Number is:",a)
# elif b >= a and b >= c:
#     print("Largest number is:",b)
# else:
#     print("Largest number is:",c)


#4) check whether number is neutral,positive,negative using ladder if statement
n = int(input("Enter a number:"))
if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Neutral")