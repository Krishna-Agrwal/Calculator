print("---Welcome---")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponential or Power")
print("6. Percentage")

def calculator():

    
    operation = input("What Calculation do you want to perform:")
    if operation == "+" or operation == "Additon" or operation == "1" or operation == "Add" or operation == "add":
        input_1 = int(input("Enter the First Number :")) #To take the first value from the user
        input_2 = int(input("Enter the Second Number:")) #To take the second value from the user
        output_1 = input_1 + input_2
        print("Additon:",output_1)
    elif operation == "-" or operation == "Substraction" or operation == "2"or operation == "Sub" or operation == "sub":
        input_1 = int(input("Enter the First Number :")) #To take the first value from the user
        input_2 = int(input("Enter the Second Number:")) #To take the second value from the user
        output_2 = input_1 - input_2
        print("Substraction:",output_2)
    elif operation == "*" or operation == "Multiplication" or operation == "3"or operation == "Multiply" or operation == "multiply" or operation == "x":
        input_1 = int(input("Enter the First Number :")) #To take the first value from the user
        input_2 = int(input("Enter the Second Number:")) #To take the second value from the user
        output_3 = input_1 * input_2
        print("Multiplication:",output_3)
    elif operation == "/" or operation == "Division" or operation == "4"or operation == "Divide" or operation == "divide":
        input_1 = int(input("Enter the First Number :")) #To take the first value from the user
        input_2 = int(input("Enter the Second Number:")) #To take the second value from the user        
        output_4 = input_1 / input_2
        print("Divison:",output_4)
    elif operation == "**" or operation == "Exponential" or operation == "power" or operation == "5" or operation == "Power":
        input_1 = int(input("Enter the First Number :")) #To take the first value from the user
        input_2 = int(input("Enter the Second Number:")) #To take the second value from the user        
        output_5 = input_1 ** input_2
        print("Exponential:",output_5)
    elif operation == "%" or operation == "Percetange" or operation == "6"or operation == "percentage":
        input_1 = int(input("Enter the First Number :")) #To take the first value from the user
        input_2 = int(input("Enter the Second Number:")) #To take the second value from the user
        output_6 = input_1 % input_2
        print("Percentage:",output_6,"%")
    else:
        print("Kindly Make a Perfect Choice")
        print("Thank you")
    
    another_Calculation = input("Do you want to make more calculation: ")
    if another_Calculation == "yes" or another_Calculation == "Yes" or another_Calculation == "y" or another_Calculation == "Y":
        calculator()
    else:
        print("Thank you")

calculator()
