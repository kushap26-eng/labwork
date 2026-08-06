#1) create a list of five fruits,print second and last fruit,add mango to the list and remove the first element
# sort the list alphabatically and reverse it

# fruits = ["Apple","Banana","Orange","Grapes","Cherry"]
# print("Second Fruit: ",fruits[1])
# print("Last Fruit: ",fruits[-1])

# fruits.append("Mango")
# print("After adding Mango: ",fruits)
# fruits.pop(0)
# print("After removing first element: ",fruits)

# fruits.sort()
# print("Sorted List: ",fruits)
# fruits.reverse()
# print("Reversed List: ",fruits)



#2) Create a tuple of 5 numbes.
# Access the third item in tuple
# try to change the second value and observe the result(Explain mutability)

# numbers = (10,20,30,40,50)
# print("Third Item: ",numbers[2])
# try:
#     numbers[1] = 25
# except TypeError as e:
#     print("Error: ",e)
# print("Tuple are immutable, so their values cannot be changed.")



#3) Create a list and tuple both containing the same 3 items.
# try chanaging the first item of each.
# Discuss the error (in case of tuple) and explain why it happens.

# my_list = [1,2,3]
# my_tuple = (1,2,3)
# my_list[0] = 100 
# print("Modified List: ",my_list)
# try:
#     my_tuple[0] = 100
# except TypeError as e:
#     print("Error: ",e)
# print("Lists are mutable, but tuples are immutable.")



#4) Create a list of squares of numbres from 1 to 10 using list comprehension.
# Create a new list that only contains even numbers from given list [1,2,3.....,20].
# convert all strings in a list ["hello","WORLD","PyThOn"] to lowercase using list comprehension

squares = [x**2 for x in range(1,11)]
print("Squares: ",squares)

even_numbers = [x for x in range (1,21) if x % 2 == 0]
print("Even Numbers: ",even_numbers)

words = ["hello","WORLD","PyThOn"]
lowercase_words = [word.lower() for word in words]
print("Lowercase Strngs: ",lowercase_words)
