#1 example

a = 5
b = 2
if a > b: print("a is greater than b") #returns : a is greater than b

#2 example

a = 2
b = 330
print("A") if a > b else print("B") #returns : B

#3 example

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger) #returns : "Bigger is 20"

#4 example

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #returns : =

#5 example

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name) #returns : "Welcome, Guest"