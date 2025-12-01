def perform_operation(num1, num2, operation):
    if operation == "add":
        num1 + num2
    elif operation == "subtract":
        num1 - num2
    elif operation == "multiply":
        num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return print('Cannot devide by 0')
        else:    
            num1 / num2


