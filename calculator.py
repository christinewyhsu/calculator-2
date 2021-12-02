"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

#  reduce function can help functions in arithmetic take in a list of numbers
from functools import reduce

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
    num_list = [float(x) for x in tokens[1:]]

    result = None
    if operator == '+':
        result = reduce(add, num_list)

    elif operator == '-':
        result = reduce(subtract, num_list)

    elif operator == '*':
        result = reduce(multiply, num_list)

    elif operator == '/':
        result = round(reduce(divide, num_list),2)

    elif operator == 'square':
        result = [square(x) for x in num_list] if len(num_list) > 1 else square(num_list[0])

    elif operator == 'cube':
        result = [cube(x) for x in num_list] if len(num_list) > 1 else cube(num_list[0])

    elif operator == 'pow':
        result = reduce(power, num_list)

    elif operator == 'mod':
        result = reduce(mod, num_list)
    
    else:
        result = 'Please enter an operator followed by two integers'
    
    print(result)