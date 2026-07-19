# 1) Write a Python program that:
# Uses a for loop to print numbers from 1 to 20.
# Skip numbers divisible by 4 using the continue statement.

for i in range(1,21):
    if i % 4 == 0:
        continue
    print(i)

#2) Implement a program using a while loop to:
# Print numbers from 1 to 10.
# Stop the loop using the break statement when the number is 7.

num = 1
while num <= 10:
    if num == 7:
        break
    print(num)
    num += 1


# 3) Create a program that:
# Iterates over a string (e.g., "PYTHON").
# Uses a continue statement to skip vowels and print only consonants.

word = "PYTHON"
for ch in word:
    if ch.upper() in "AEIOU":
        continue
    print(ch)



#4) Write a Python program to print multiplication tables using nested loops for up to N numbers in this format:
# 1 x 1 = 1
# 1 x 2 = 2
# …
# Where N is the user-given number.

# n = int(input("Enetr the value of N:"))
# for i in range(1,n+1):
#     print("\nTable of",i)
#     for j in range(1,11):
#         print(i, "x", j, "=", i*j)  



#5) Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = " ")
    print("")


#6) Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j,end =" ")
    print("")


#7) Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end = " ")
    print()


#8) Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

for i in range(1,6):
    for j in range(i,6):
        print(j,end= " ")
    print("")