# 1) Create a set of integers: {1, 2, 3, 4, 5}.
# Add 6, remove 3, and check if 2 is in the set.
# set = {1,2,3,4,5}
# set.add(6)
# set.remove(3)
# print("Set: ",set)
# print("Is 2 in the set?",2 in set)



#2) Perform the following operations on the given two sets:
# Union
# Intersection
# Difference
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# set_a = {1,2,3,4}
# set_b = {3,4,5,6}
# print("Union: ",set_a | set_b)
# print("Intersection: ",set_a & set_b)
# print("Differnce(a-b): ",set_a-set_b)



#3) Create a dictionary:
# student = {"name": "Alice", "age": 20, "grade": "A"}
# Print the keys and values
# Add a new key: "city": "Delhi"
# Update "age" to 21
# Delete the "grade" key

# student = {
#     "name" : "Kushangi",
#     "age" : 22,
#     "grade" : "A"
# }
# print("Keys: ",student.keys())
# print("Values: ",student.values())
# student["city"] = "Delhi"
# student["age"] = 21
# del student["grade"]
# print("Updated Dictionery: ",student)



#4) Create a dictionary from two lists:
# keys = ['id', 'name', 'email']
# values = [101, 'Bob', 'bob@example.com']

# keys =["id", "name" , "email"]
# values = [101, "Kusha", "kusham@example.com"]
# student = dict(zip(keys,values))
# print(student)


#5) Convert the following:
# A string '123' to an integer
# A list [1, 2, 3] to a tuple
# A tuple (4, 5, 6) to a list
# A list of pairs [(1, 'A'), (2, 'B')] to a dictionary

# num = int("123")
# print(num)
# lst = [1,2,3]
# tup = tuple(lst)
# print(tup)
# t = (4,5,6)
# lst2 = list(t)
# print(lst2)
# pairs = [(1, 'A'),(2, 'B')]
# d = dict(pairs)
# print(d)


#6) Delete a specific item from a list using del keyword.
# numbers = [10,20,30,40,50]
# del numbers[2]
# print(numbers)