a = int(input("Enter number a\n"))
b = int(input("Enter number b\n"))

oper = input("Enter Operator: +, -, /, *\n")

if (oper == "+"):
    print("The sum of a and b is ", a + b)
elif (oper == "-"):
    print("The subtraction of a and b is ", a  - b)
elif (oper == "*"):
    print("The multiplication of a and b is ", a * b)
elif (oper == "/"):
    print("The division of a and b is ", a / b)
else:
    print("Invalid operator is given. Please enter correct operator.")
