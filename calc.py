# Supported operations
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    'x': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

# Get input
user_input = input('Calc_67: \n> ')

# Splitting
parts = user_input.split()

# No Input
if len(parts) == 0:
    print('No input')
    exit()
    
# Single digit (No operation)
if len(parts) == 1:
    try:
        result = float(parts[0])
        print('Result:', result)
    except ValueError:
        print('Syntax Error')
        exit()

# correct operator & number format
if len(parts) % 2 == 0:
    print('Syntax Error')
    exit()

try:
    result = float(parts[0])
    # loop to get operator and num pairs
    for i in range(1, len(parts), 2):
        operator = parts[i]
        num = float(parts[i+1])
        
        if operator not in operations:
            print(f'Unsupported operator: {operator}')
    
        result = operations[operator](result, num)
        
    if result == int(result):
        formatted = f'{int(result):,}'.replace(',', '.')
    else:
        formatted = f'{result:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

    print('Result:', formatted)

except ValueError:
    print('Syntax Error')