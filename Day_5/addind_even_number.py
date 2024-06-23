#You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
#i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
#Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.
#Example Input 1
#10
#Example Output 1
#30
#Example Input 2
#52
#Example Output 2
#702
#Hint
#There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

sum = 0
n=int(input("Enter the number till which the number needs to be added "))
for num in range(0,n+2,2):
    sum+=num
print(f"The sum of all even number between 0 and {n} is {sum}")