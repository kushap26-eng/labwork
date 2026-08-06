# data types
#1) first name and last name
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Hello, {last_name}, {first_name}!")


#2) format sentence using f-string
item = "apple"
price = 5.50
print(f"The price of {item} is {price} dollars.")


#3) Reverse string and check palindrome
# text = input("Enter a string: ")
# reversed_text = text[::-1]
# print("Reversed String: ",reversed_text)
# if text == reversed_text:
#     print("It is a palindrome.")
# else:
#     print("It is not palindrome.")

#4) Convert String to Uppercase, Lowercase, and Title Case
# text = input("Enter a String:")
# print("Uppercase: ",text.upper())
# print("Lowercase: ",text.lower())
# print("Title case: ",text.title())


#5) String Operation
# sentence = "Machine Learning and AI are trending"
# position = sentence.find("AI")
# print("Position of AI: ",position)
# new_sentence = sentence.replace("AI","Artificial Intelligence")
# print("After Replacement:",new_sentence)
# text = "data data mining and big data"
# count = text.count("data")
# print("Count of 'data':",count)



#6) Split,Join and multiline string
fruits = "apple,banana,grapes"
fruit_list = fruits.split(",")
print("Split List:",fruit_list)

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Joined Sentence:",sentence)

text = """Line1
Line2
Line3"""

lines = text.splitlines()
print("Separate Lines:")
for line in lines:
    print(line)



#7) Startwith, Endwith,Remove Non-Alphanumaric,Reverse String
text = "Hello Python World"
print("Starts with 'Hello':",text.startswith("Hello"))
print("End with 'World':",text.endswith("World"))

text2 = "Data123#Science"
cleaned =""
for char in text2:
    if char.isalnum():
        cleaned += char
print("Cleaned String:",cleaned)

word = "Python"
print("Reversed String:",word[::-1])