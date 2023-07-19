print("welcome to the simple calculator")
num1 = int(input("enter your first number: \n"))
operator = input("enter the operation you want to do on the numbers i.e add,  sub , times or divide: \n")
num2 = int(input("enter your second number: \n"))
if operator == "add": 
 print(f"your answer is {num1 + num2}")
elif operator == "sub": 
 print(f"your answer is {num1 - num2}")
elif operator == "times": 
 print(f"your answer is {num1 * num2}")
elif operator == "divide" and num2 == 0: 
 print(f"can't divide with zero")
elif operator == "divide": 
 print(f"your answer is {num1 / num2}")
else: 
 print("operation is not recognized. please enter the selected operation names, i.e add,  sub, times or divide")