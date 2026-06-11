#1 example
#Almost any value with content evaluates to True
print(bool("Hello"))  # Output: True
print(bool(15))       # Output: True
print(bool(["apple", "banana"]))  # Output: True

#2 example: Some values are False 
#Empty values always evaluate to False
print(bool(False))  # Output: False
print(bool(None))   # Output: False
print(bool(0))      # Output: False
print(bool(""))     # Output: False
print(bool([]))     # Output: False

