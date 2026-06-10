#1 example 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#2 example

x = 1
y = 35656222554887711
z = -3255522

print(type(x)) #<class 'int'>
print(type(y)) #<class 'int'>
print(type(z)) #<class 'int'>

#3 example

x = 1.10
y = -35.59
z = 12E4
f = -87.7e100

print(type(x)) #<class 'float'>
print(type(y)) #<class 'float'>
print(type(z)) #<class 'float'>
print(type(f)) #<class 'float'>


 
#4 example

x = 3+5j
y = 5j
z = -5j

print(type(x)) #<class 'complex'>
print(type(y)) #<class 'complex'>
print(type(z)) #<class 'complex'>

#5 example

x = 1        # int
y = 2.8      # float
z = 1j       # complex

# conversion
a = float(x)      # int to float
b = int(y)        # float to int
c = complex(x)    # int to complex

print(a)
print(b)
print(c)

print(type(a))  # <class 'float'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'complex'>