def greet() :
    print("Hello")
    print("How do you do ? ")
    print("Isn't the weather nice today?")


#Function that allow input

def greet_with_name(name) :
    print(f"Hello{name}")
    print(f"How do you do ?{name} ")
    print(f"Hi {name}Isn't the weather nice today?")


name = str(input("What's your name"))
print(greet_with_name())