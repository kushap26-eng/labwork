#1) Write a program using a `while` loop to:
#Take numbers as input from the user until they enter `0`.
# while True:
#     num = int(input("Enter a number(0 to stop):"))
#     if num == 0:
#         break
#     print("You entered:",num)


#2) Create a program using a `for` loop to:
# Iterate over a given range(1 to 10).
#  Print each digit’s square, one per line.

# for i in range(1,11):
#     print(i * i)


# 3) Write a program to:
# Use a `while` loop to print all even numbers between 1 and 50.
# num = 2
# while num <= 50:
#     print(num)
#     num += 2


#4) Write a program to:
# Use the `range()` function to generate a sequence of numbers from 1 to 20.
# Print only the odd numbers using a `for` loop.
# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)


#5)Implement a program that:
#Uses the `range()` function with three arguments (start, stop, step) to print multiples of 5 from 5 to 50.
# for i in range(5,51,5):
#     print(i)
#multiple of 3
# for i in range(3,31,3):
#     print(i)


#6) Create a program using a `for` loop and `range()` to:
#Print a reverse countdown from 10 to 1.
for i in range(10,0,-1):
    print(i)



#7) Write a program that:
# Uses a `for` loop and `range()` to iterate through numbers from 1 to 50.
# Checks if each number is divisible by 2, 3, or both using nested `if-elif-else`.
# Prints messages for each case (e.g., "Divisible by 2", "Divisible by 3", "Divisible by both").
for i in range(1,51):
    if i % 2 == 0 and i % 3 == 0:
        print(i,"- Divisible by both 2 and 3")
    elif i % 2 == 0:
        print(i,"- Divsible by 2")
    elif i % 3 == 0:
        print(i,"- Divisible by 3")
    else:
        print(i,"- Not divisible by 2 and 3")