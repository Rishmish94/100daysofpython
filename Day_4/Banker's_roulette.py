import random
name = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
print(len(name))
random_choice = random.randint(0,len(name)-1)
random_name = name[random_choice]
print(f"The Person going to pay today's bill is {random_name}")