#Prompt the user to enter an operator for the calculation
operator = input("enter an operator(+, -,*,/): ")

# Ask the user to input two numbers and convert them to integer/ floating values
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

#calculation if the operator is addition "+" 
if operator == "+": 
    result = num1 +num2
    print(result)
#calculation if the operator is subtraction "-"
elif operator == "-":
    result= num1-num2
    print(result)

#calculation if the operator is multiplication "*"
elif operator == "*":
    result = num1 *num2
    print(result)

#calculation if the operator is division "/"
elif operator == "/":
    if num2 != 0 :    #If the num2 is not equal to 0
         result = num1/num2    
         print(result)

#display to be seen when a number is divided by zero         
    else:
        print("number cannot be divided by 0") 

#display to be seen when wrong operator has been used        
else:
    print("invalid choice! Please select valid operator")   





