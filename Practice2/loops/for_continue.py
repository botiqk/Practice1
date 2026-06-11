#1 example

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#2 example

i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i) # 1 2 4 5 6 7 8 9