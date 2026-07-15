# 1) Type casting Consturctor
# value = input("Enter a value:")
# int_value = int(value)
# float_value = float(value)
# str_value = str(value)
# bool_value = bool(value)
# print("Integer =",int_value,type(int_value))
# print("Float =",float_value,type(float_value))
# print("String =",str_value,type(str_value))
# print("Boolean =",bool_value,type(bool_value))


#2) Convert float into interger
# num = float(input("Enter a floating point number:"))
# int_num = int(num)
# print("Original float value =",num)
# print("Converted Integer value =",int_num)
# print("int()removes the decimal part of the number.")


#3) Boolean to integer and string
# bool_value = input("Enter True or False:") == "True"
# int_value = int(bool_value)
# str_value = str(bool_value)
# print("Boolean Value:",bool_value)
# print("Interger Valye:",int_value)
# print("String Value:",str_value)


#4) Display Value, Type and memory address
a = 100
b = 10.5
c = "Python"
d = True
e = [1,2,3]
f = (4,5,6)
g = {"name": "Kushangi","age":21}

print(a,type(a),id(a))
print(b,type(b),id(b))
print(c,type(c),id(c))
print(d,type(d),id(d))
print(e,type(e),id(e))
print(f,type(f),id(f))
print(g,type(g),id(g))


#5) Memory address using id()
a = 100
b = 100
print("Before Modification")
print("a =",a,"Address =",id(a))
print("b =",b,"Address =",id(b))
if id(a) == id(b):
    print("Both variables have same memory address.")
else:
    print("Both variables have different memory address.")

b = 200
print("\nAfter Modification")
print("a =",a,"Address =",id(a))
print("b =",b,"Address =",id(b))
if id(a) == id(b):
    print("Both variables have same memory address.")
else:
    print("Both variables have diffrent memory address.")
