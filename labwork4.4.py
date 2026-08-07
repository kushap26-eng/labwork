#Write a Program to find the length of a 1D array without using any built-in function.
# n = int(input("Enter array size: "))
# a = []
# print("Enter array elements: ")
# for i in range(n):
#     element =int(input(f"a[{i}] = "))
#     a.append(element)
# count = 0
# for i in a:
#     count = count +1 
# print("Length of array: ",count)



#2) Write a Program to find the average of a 1D array without using any built-in function.
# def average(a):
#     total = 0
#     count = 0
#     for element in a:
#         total = total +element
#         count = count + 1
#     average = total/count
#     return average

# n = int(input("Enter array size: "))
# a = []
# print("Enter array element: ")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
# average = average(a)
# print("average of an Array: ",average)


#3) Write a Program to perform the addition operation of two 1D arrays & store it in another array. Keep in mind that both array sizes must be the same.
# array1 = int(input("Enter first array size: "))
# array2 = int(input("Enter second array sze: "))
# if array1 == array2:
#     a = []
#     b = []
#     c = []
#     print("Enter first array elements: ")
#     for i in range(array1):
#         element = int(input(f"a[{i}]: "))
#         a.append(element)
#     print("Enter second array elements: ")
#     for i in range(array2):
#         element = int(input(f"b[{i}]: "))
#         b.append(element)
#     for i in range(array1):
#         c.append(a[i] + b[i])
#     print("Addition of two array: ",c)
# else:
#     print("Array sizes must be same.")



#4) Create an array of numbers from 1 to 10.
#Multiply each element by 2 and print the result.
# array = []
# array2 = []
# for i in range(1,11):
#     array.append(i)
# for i in range(10):
#     array2.append(array[i]*2)
# print(array2)



#5) Take user input for a number.
# Check if it exists in the array.
# Print the index if found, else print "Not Found".

# array = [10,30,80,90,60]
# num = int(input("Enter a number: "))
# found = False
# for i in range(5):
#     if array[i]== num:
#         print("Index:",i)
#         found = True
#         break
# if found == False:
#     print("Not Found.")


#6) In a user-defined array (by taking input):
# Print all even numbers from the array.
# Print all odd numbers from the array.
# n = int(input("Enter Array Size: "))
# a = []
# print("Enter array elements: ")
# for i in range(n):
#     element = int(input(f"a[{i}]: "))
#     a.append(element)
# print("Even Numbers")
# for i in range(n):
#     if a[i] % 2 == 0:
#         print(a[i])
# print("Odd numbers")
# for i in range(n):
#     if a[i] % 2 != 0:
#         print(a[i])


# second method
# even_number= []
# odd_number = []
# for num in a:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
# print("Even nuber: ",even_numbers)
# print("Odd numbers: ",odd numbers)


#7) In a 1D Array:
# Print the first five elements.
# Print every alternate element from the array.
# a = [10,20,30,40,50,60,70,80]
# print("First FIve Elements: ")
# for i in range(5):
#     print(a[i])
# print("Alternate Elelments: ")
# for i in range(0,8,2):
#     print(a[i])


#8) Print the first, last, and middle elements of the array.
array = [10,20,30,40,50,60,70]
n = 0
for element in array:
    n = n + 1
print("First Elelment:",array[0])
print("Last Elelment:",array[n-1])
middle = n // 2
print("Middle Elelment",array[middle])