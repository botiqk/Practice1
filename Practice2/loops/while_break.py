#1 example 

while True:
    word = input("Say something (or 'stop'): ")
    if word == "stop":
        break  
    print("You said", word)

#2 example

while True:
    password = input("Enter password: ")
    if password == "secret123":
        print("Access granted!")
        break
    print("Wrong password. Try again.")
