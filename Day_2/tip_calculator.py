print("Welcome to tip calculator")
Total = int(input("What was the total bill?  Rs"))
Tip = int(input("How much tip do you want to give in person ?  (in percent)"))
split = int(input("How many people to split the bill? "))
per_person_pay = ( Total + ((Total*Tip)/100))/split
print(f"Each Person should pay : Rs {per_person_pay}") 