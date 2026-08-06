# 1D Array
#1) Create a 1D array(list) with 5 integer elements.Display the array using a loop.
# array = [1,2,3,4,5]
# for i in array:
#     print(i)


#2) Develop a program to calculate the sum of all elements in a 1D array.
# array = [1,2,3,4,5]
# sum = 0
# for i in array:
#     sum = sum + i
# print("Sum of Array elements: ",sum)


#3) create a program to insert a new element at a specific position in 1D array
# array = [1,2,3,4,5]
# value = int(input("Enter Value: "))
# position = int(input("Enter position: "))

# array.insert(position-1,value)
# print("Updated Array: ")
# print(array)



#4) Write a program to delete an element by its value from a 1D array
# array = [1,2,3,4,5]
# print(array)
# value = int(input("Enter value to delete: "))
# if value in array:
#     index = array.index(value)
#     del array[index]
#     print("Updated Array:")
#     print(array)
# else:
#     print("Value not found")


#5) Develop a program to update an element in a 1D array based on its index
# array = [1,2,3,4,5]
# print(array)
# index = int(input("Enter index:"))
# value = int(input("Enter new value: "))
# array[index]= value
# print("Updataed Array: ",array )


#6) Implement a program to search for an element in a 1D array and return its value
# array = [1,2,3,4,5]
# print(array)
# value = int(input("Enter value to search: "))
# if value in array:
#     print("Element found at index",array.index(value))
# else:
#     print("Element not found")


#7) Write a program to concatenate two 1D arrays into a single array
# array1 = [1,2,3,4]
# array2 = [5,6,7,8]
# array3 = array1 + array2
# print("Concatenated Array: ")
# print(array3)