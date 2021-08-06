#QUESTION2
def calculate_factorial(num):
    if (num ==0):
        return 1
    else:
        return num*calculate_factorial(num-1)
number=int(input("Enter the number you want to calculate it's factorial  "))
result=calculate_factorial(number)
print("The factorial of the number is =",result)