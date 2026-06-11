#$python strings
#1 example 

print("Hello", "how are you?", sep="---") #Hello---how are you?

#2 example

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

#3 example 

txt = "The best things in life are free!"
print("free" in txt) #returns True

#$slicing strings 
#1 example

b = "Hello, World!"
print(b[-5:-2]) #orl

#$modify strings
#1 example

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#2 example

a = "Hello, World!"
print(a.replace("H", "J")) #returns "Jello, World!"

#3 example

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#$concatenate strings
#1 example 

a = "Hello"
b = "World"
c = a + b
print(c)

#$format strings
#1 example

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#2 example

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #returns "The price is 59.00 dollars"

#$escape char
#1 example
txt = "We are the so-called \"Vikings\" from the north." #returns "We are the so-called "Vikings" from the north."