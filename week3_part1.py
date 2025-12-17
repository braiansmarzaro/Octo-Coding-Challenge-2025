def evaluate_rpn(expression):
    """Evaluate a mathematical expression in Reverse Polish Notation.
    
    Args:
        expression (str): The RPN expression as a string with space-separated tokens.
    
    Returns:
        float: The result of the evaluated expression.
    """
    stack = []
    tokens = expression.strip().split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            # Pop two operands from the stack
            if len(stack) < 2:
                raise ValueError(f"Invalid RPN expression: not enough operands for operator {token}")
            
            b = stack.pop()
            a = stack.pop()
            
            # Perform the operation
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            
            stack.append(result)
        else:
            # It's a number, push it onto the stack
            try:
                stack.append(int(token))
            except ValueError:
                try:
                    stack.append(float(token))
                except ValueError:
                    raise ValueError(f"Invalid token: {token}")
    
    # The final result should be the only item left on the stack
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: too many operands")
    
    return stack[0]


# Read the RPN expression from the file
with open('3_1.txt', 'r') as file:
    rpn_expression = file.read().strip()

print(f"RPN Expression: {rpn_expression}")

# Evaluate the expression
result = evaluate_rpn(rpn_expression)

print(f"Result: {result}")
