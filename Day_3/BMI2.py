# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

Weight = int(input("Enter your weight in Kg "))
Height = float(input("Enter your height in m "))
BMI = Weight/(Height)**2
if BMI < 18.5 :
    print(f"Your BMI is {BMI} and You are underweight")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI} and You have a normal weight")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI} and You are slightly overweight")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI} and You are obese")
elif BMI > 35:
    print(f"Your BMI is {BMI} and You are clinically obese")
