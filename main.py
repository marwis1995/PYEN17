from email.policy import strict

print("Hello world")

#Variables - like a box with some content, and with 'label'

message = "Hello world"
print(message)

message = message +  " World"
print(message)

message = "aaaaaa"
print(message)

#==========================Basic data types=========================
#Integer (number)
counter = 2
print(counter)

#Floating-point (number)
weight_sum = 10.5
print(weight_sum)

#String (text)
message = "Future Collars"
print(message)

#Multiline string
message2 = """
line1
line2
line3
"""
print(message2)

#Boolean value - True/False
always_true = True
print(always_true)

always_false = False
print(always_false)

#None - nothing
nothing_here = None
print(nothing_here)


#=================================Math operators==========================
a = 2
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b % a) #Remainder from divide 11 % 2 -> 2 + 2 + 2 + 2 + 2 + 1
print(a ** b) #To the power of (2 * 2 * 2)


#==============================Logical operators=========================
print(a == b) #Equals
print(a != b) #Different
print(a < b) #Less
print(a <= b) #Less or eq
print(a > b) #Grater
print(a >= b) #Greater or eq


#=======================AND, OR, NOT operators========================
#AND - both are True
print(False and False) #False
print(False and True) #False
print(True and False) #False
print(True and True) #True

#OR - at least one is true
print(False or False) #False
print(False or True) #True
print(True or False) #True
print(True or True) #True

#NOT - negation
print(not True) #False
print(not False) #True


#=============================Variables in boolean context====================
print()
print()
print(bool(-1)) #True
print(bool(0)) #False
print(bool(1)) #True
print(bool(2)) #True
print(bool(0.1)) #True
print(bool("")) #False
print(bool("something")) #True
print(bool(" ")) #True
print(bool(None)) #False


#==============================Checking variable type=========================
a = "Text"
print(type(a)) #Check variable type

print(type(a) is str)
print(type(a) == str) #Not recommended
print(type(a) is int)
print(type(a) is not int)


print(1 + 2) #Add like number
print("1" + "2") #Concatenating the strings

print(int("1") + int("2")) #Change type string to int
print(str(1) + str(2)) #Change type int to string

print(bool(-1)) #True
print(bool(0)) #False
print(bool(1)) #True


message = "new message"
print(message)

message = 2
print(message)


#=================================Text operations=============================
print("Hello" + " " + "world") #String concatenation
print("Hello" * 5) #Multiply a string
print("Text for %s formatting %i" % ("a", 2)) #Deprecated
a = "Word"
print("My program prints hello {}".format(a))
print("My program prints hello {} in line {}".format(a, 135))

print(f"Hello {a}!")


#=============================Getting user input==============================
print("What's your name?")
user_name = input()
print("Hello {}".format(user_name))

age = int(input("How old are you?"))
print("Your age is {}".format(age))
print("In ten years you will be {} years old".format(age + 10))


#==========================Additional text formatting========================
print("1\n2\n3\n4\n5") #\n to brake the line
print("My favourite book is \"The Alchemist\" John Doe") #Escape character
print("My favourite book is 'The Alchemist' John Doe")