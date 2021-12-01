"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input('Enter your equation > ')
    tokens = user_input.split(' ')

    # Conditions to terminate the program or prompt the user to input valid arguments
    if 'q' in tokens or 'quit' in tokens:
        print('You will exit calculator program')
        break
    elif len(tokens) < 2:
        print('Not enough input arguments. Try again')
        continue

    operator = tokens[0]
    num1 = float(tokens[1])

    if len(tokens) > 2:
        num2 = float(tokens[2])

    result = None
    if operator == '+':
        result = add(num1, num2)

    elif operator == '-':
        result = subtract(num1, num2)

    elif operator == '*':
        result = multiply(num1, num2)

    elif operator == '/':
        result = divide(num1, num2)

    elif operator == 'square':
        result = square(num1)

    elif operator == 'cube':
        result = cube(num1)

    elif operator == 'pow':
        result = power(num1, num2)

    elif operator == 'mod':
        result = mod(num1, num2)
    
    else:
        result = 'Please enter an operator followed by two integers'
    
    print(result)