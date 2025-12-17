import re
# Under 130 lines of code

# Parse the specification and build a dependency graph
requirements = {}

spec_text = """
Requirement 1.1: Secret Number
The sum of Number-1.93 and Number-1.18.
Requirement 1.2: Aggregate Coefficient
Number-1.151 plus Number-1.31.
Requirement 1.3: Product Term
The product of Number-1.128 and Number-1.141.
Requirement 1.4: Difference Metric
Number-1.131 minus Number-1.32.
Requirement 1.5: Baseline Offset
A fixed constant equal to -36788.
Requirement 1.6: Scaling Pair
Multiply Number-1.115 by Number-1.36.
Requirement 1.7: Composite Gain
Number-1.95 times Number-1.69.
Requirement 1.8: Static Bias
Constant value -9264.
Requirement 1.9: Unit Increment
Constant equal to 125.
Requirement 1.10: Negative Anchor
Constant value -64487.
Requirement 1.11: Downshift
Constant set to -21643.
Requirement 1.12: Identity Constant
Constant equal to 1.
Requirement 1.13: Inverse Unit
Constant equal to -1.
Requirement 1.14: Quotient Node
Number-1.4 divided by Number-1.88.
Requirement 1.15: Dual Unit
Constant equal to 2.
Requirement 1.16: Negative Baseline
Constant value -28275.
Requirement 1.17: Deep Negative
Constant value -83234.
Requirement 1.18: Summation Bridge
Add Number-1.54 to Number-1.67.
Requirement 1.19: High Marker
Constant equal to 89133.
Requirement 1.20: Midpoint Level
Constant equal to 62054.
Requirement 1.21: Reference Level
Constant equal to 35398.
Requirement 1.22: Cross Product
Number-1.142 multiplied by Number-1.135.
Requirement 1.23: Offset Delta
Number-1.159 less Number-1.19.
Requirement 1.24: Amplification Term
Number-1.120 times Number-1.86.
Requirement 1.25: Division Factor
Number-1.58 over Number-1.103.
Requirement 1.26: Subtractive Link
Number-1.57 subtracted by Number-1.134.
Requirement 1.27: Multiplier Node
Number-1.132 times Number-1.156.
Requirement 1.28: Sum Connector
Number-1.70 added to Number-1.123.
Requirement 1.29: Fixed Quantity
Constant equal to 37888.
Requirement 1.30: Ratio Term
Number-1.117 divided by Number-1.126.
Requirement 1.31: Difference Link
Number-1.64 minus Number-1.138.
Requirement 1.32: Delta Node
Number-1.155 less Number-1.110.
Requirement 1.33: Product Chain
Number-1.107 multiplied by Number-1.3.
Requirement 1.34: Negative Constant
Constant equal to -13550.
Requirement 1.35: Factor Blend
Number-1.143 times Number-1.12.
Requirement 1.36: Composite Scale
Number-1.15 multiplied by Number-1.26.
Requirement 1.37: Pairwise Product
Number-1.122 times Number-1.133.
Requirement 1.38: Additive Merge
Number-1.23 plus Number-1.96.
Requirement 1.39: Unity
Constant equal to 1.
Requirement 1.40: Accumulated Sum
Number-1.158 added to Number-1.153.
Requirement 1.41: Subtraction Metric
Number-1.16 minus Number-1.92.
Requirement 1.42: Gain Product
Number-1.65 times Number-1.106.
Requirement 1.43: Quotient Factor
Number-1.111 over Number-1.82.
Requirement 1.44: Upper Marker
Constant equal to 77733.
Requirement 1.45: Compound Product
Number-1.42 multiplied by Number-1.50.
Requirement 1.46: Negative Drift
Constant value -38983.
Requirement 1.47: Binary Unit
Constant equal to 2.
Requirement 1.48: Large Negative
Constant value -94024.
Requirement 1.49: Division Bridge
Number-1.24 divided by Number-1.13.
Requirement 1.50: Moderate Constant
Constant equal to 38.
Requirement 1.51: Positive Marker
Constant equal to 42315.
Requirement 1.52: Unit Value
Constant equal to 1.
Requirement 1.53: Difference Gate
Number-1.152 less Number-1.22.
Requirement 1.54: Multiplicative Term
Number-1.7 times Number-1.98.
Requirement 1.55: Mid Positive
Constant equal to 45217.
Requirement 1.56: Scaled Unit
Number-1.52 multiplied by Number-1.127.
Requirement 1.57: Division Node
Number-1.97 over Number-1.109.
Requirement 1.58: Strong Negative
Constant equal to -90223.
Requirement 1.59: Negative Mark
Constant equal to -45773.
Requirement 1.60: High Constant
Constant equal to 90339.
Requirement 1.61: Subtractive Pair
Number-1.5 minus Number-1.53.
Requirement 1.62: Level A
Constant equal to 30113.
Requirement 1.63: Level B
Constant equal to 74525.
Requirement 1.64: Small Negative
Constant equal to -2953.
Requirement 1.65: Tiny Negative
Constant equal to -1766.
Requirement 1.66: Low Point
Constant equal to -78541.
Requirement 1.67: Additive Pair
Number-1.118 plus Number-1.72.
Requirement 1.68: Offset Down
Constant equal to -12045.
Requirement 1.69: Unit
Constant equal to 1.
Requirement 1.70: Gain Blend
Number-1.85 times Number-1.154.
Requirement 1.71: Pair Sum
Number-1.147 added to Number-1.124.
Requirement 1.72: Large Downshift
Constant equal to -77033.
Requirement 1.73: Positive Tick
Constant equal to 11642.
Requirement 1.74: Small Positive
Constant equal to 6911.
Requirement 1.75: Linked Sum
Number-1.20 plus Number-1.89.
Requirement 1.76: Additive Blend
Number-1.157 plus Number-1.87.
Requirement 1.77: Negative Unit
Constant equal to -1.
Requirement 1.78: Top End
Constant equal to 99588.
Requirement 1.79: Sum Pair
Number-1.146 plus Number-1.51.
Requirement 1.80: Weighted Factor
Number-1.121 multiplied by Number-1.71.
Requirement 1.81: Minor Positive
Constant equal to 2359.
Requirement 1.82: Difference Pair
Number-1.27 less Number-1.136.
Requirement 1.83: Additive Gate
Number-1.99 plus Number-1.29.
Requirement 1.84: Product Blend
Number-1.100 times Number-1.112.
Requirement 1.85: Ratio Link
Number-1.90 divided by Number-1.116.
Requirement 1.86: Base Positive
Constant equal to 1357.
Requirement 1.87: Gain Pair
Number-1.149 times Number-1.81.
Requirement 1.88: Ten Constant
Constant equal to 10.
Requirement 1.89: Amplified Sum
Number-1.40 multiplied by Number-1.119.
Requirement 1.90: Strong Positive
Constant equal to 74685.
Requirement 1.91: Deep Down
Constant equal to -28522.
Requirement 1.92: Merged Sum
Number-1.84 plus Number-1.130.
Requirement 1.93: Subtractive Link B
Number-1.10 minus Number-1.114.
Requirement 1.94: Division Pair
Number-1.35 over Number-1.59.
Requirement 1.95: Quotient Bridge
Number-1.25 divided by Number-1.56.
Requirement 1.96: Positive Level
Constant equal to 26629.
Requirement 1.97: Minor Negative
Constant equal to -4690.
Requirement 1.98: Product Pair
Number-1.94 multiplied by Number-1.74.
Requirement 1.99: Delta Bridge
Number-1.160 less Number-1.37.
Requirement 1.100: Ternary Unit
Constant equal to 3.
Requirement 1.101: Extreme Negative
Constant equal to -99587.
Requirement 1.102: Simple Ratio
Number-1.11 divided by Number-1.39.
Requirement 1.103: Minus One
Constant equal to -1.
Requirement 1.104: Negative Block
Constant equal to -46186.
Requirement 1.105: Small Gain
Constant equal to 623.
Requirement 1.106: Unit Constant
Constant equal to 1.
Requirement 1.107: Additive Link
Number-1.140 plus Number-1.49.
Requirement 1.108: Positive Marker B
Constant equal to 22463.
Requirement 1.109: Unity B
Constant equal to 1.
Requirement 1.110: Subtraction Gate
Number-1.139 minus Number-1.45.
Requirement 1.111: Difference Gate B
Number-1.137 less Number-1.30.
Requirement 1.112: Positive Base
Constant equal to 18831.
Requirement 1.113: Small Count
Constant equal to 5.
Requirement 1.114: Strong Negative B
Constant equal to -64596.
Requirement 1.115: Sum Pair B
Number-1.73 plus Number-1.8.
Requirement 1.116: Moderate Count
Constant equal to 195.
Requirement 1.117: Positive Tag
Constant equal to 18689.
Requirement 1.118: Negative Tag
Constant equal to -12966.
Requirement 1.119: Small Positive B
Constant equal to 6895.
Requirement 1.120: Small Negative B
Constant equal to -62.
Requirement 1.121: Weighted Unit
Number-1.113 multiplied by Number-1.47.
Requirement 1.122: Positive Mark B
Constant equal to 10743.
Requirement 1.123: Deep Negative B
Constant equal to -64077.
Requirement 1.124: Downshift B
Constant equal to -17151.
Requirement 1.125: Negative Mass
Constant equal to -77870.
Requirement 1.126: Additive Span
Number-1.78 plus Number-1.101.
Requirement 1.127: Positive Span
Constant equal to 12889.
Requirement 1.128: Pair Sum B
Number-1.79 added to Number-1.80.
Requirement 1.129: Negative Span
Constant equal to -74314.
Requirement 1.130: Large Negative B
Constant equal to -84968.
Requirement 1.131: Positive Span B
Constant equal to 65866.
Requirement 1.132: Unity C
Constant equal to 1.
Requirement 1.133: Quad Unit
Constant equal to 4.
Requirement 1.134: Subtractive Link C
Number-1.17 minus Number-1.66.
Requirement 1.135: Ratio Bridge B
Number-1.60 divided by Number-1.62.
Requirement 1.136: Product Unit
Number-1.105 times Number-1.9.
Requirement 1.137: Difference Span
Number-1.104 less Number-1.68.
Requirement 1.138: Positive Mass
Constant equal to 54029.
Requirement 1.139: Minor Down
Constant equal to -3102.
Requirement 1.140: Large Down
Constant equal to -84132.
Requirement 1.141: Difference Link D
Number-1.108 less Number-1.144.
Requirement 1.142: Additive Span B
Number-1.44 plus Number-1.150.
Requirement 1.143: Extreme Negative B
Constant equal to -91546.
Requirement 1.144: Positive Tag B
Constant equal to 18414.
Requirement 1.145: Composite Gain B
Number-1.2 times Number-1.41.
Requirement 1.146: Strong Down
Constant equal to -67404.
Requirement 1.147: Positive Tick B
Constant equal to 19660.
Requirement 1.148: Inverse Unit B
Constant equal to -1.
Requirement 1.149: Negative Eleven
Constant equal to -11.
Requirement 1.150: Negative Base B
Constant equal to -65932.
Requirement 1.151: Difference Pair C
Number-1.21 less Number-1.102.
Requirement 1.152: Downshift C
Constant equal to -16887.
Requirement 1.153: Quotient Tag
Number-1.91 divided by Number-1.77.
Requirement 1.154: Additive Marker
Number-1.63 plus Number-1.129.
Requirement 1.155: Difference Marker
Number-1.83 less Number-1.55.
Requirement 1.156: Ratio Marker
Number-1.125 divided by Number-1.148.
Requirement 1.157: Division Marker
Number-1.46 over Number-1.75.
Requirement 1.158: Downshift D
Constant equal to -28531.
Requirement 1.159: Difference Node D
Number-1.34 minus Number-1.48.
Requirement 1.160: Positive Cap
Constant equal to 86853.
"""

# Parse each requirement
lines = spec_text.strip().split('\n')
i = 0
while i < len(lines):
    line = lines[i].strip()
    if line.startswith('Requirement 1.'):
        # Extract requirement number
        match = re.match(r'Requirement 1\.(\d+):', line)
        if match:
            req_num = int(match.group(1))
            i += 1
            # Get the definition (next line)
            if i < len(lines):
                definition = lines[i].strip()
                requirements[req_num] = definition
    i += 1

print(f"Parsed {len(requirements)} requirements")

# Now parse each definition to extract the formula
def parse_definition(definition):
    """Parse a requirement definition and return a formula."""
    
    # Check for constant
    const_patterns = [
        r'Constant (?:equal to|value|set to) (-?\d+)',
        r'A fixed constant equal to (-?\d+)',
    ]
    for pattern in const_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('const', int(match.group(1)))
    
    # Check for operations
    # Addition patterns
    add_patterns = [
        r'Number-1\.(\d+) (?:plus|added to) Number-1\.(\d+)',
        r'Add Number-1\.(\d+) to Number-1\.(\d+)',
        r'The sum of Number-1\.(\d+) and Number-1\.(\d+)',
    ]
    for pattern in add_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('add', int(match.group(1)), int(match.group(2)))
    
    # Subtraction patterns
    sub_patterns = [
        r'Number-1\.(\d+) (?:minus|less) Number-1\.(\d+)',
        r'Number-1\.(\d+) subtracted by Number-1\.(\d+)',
    ]
    for pattern in sub_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('sub', int(match.group(1)), int(match.group(2)))
    
    # Multiplication patterns
    mul_patterns = [
        r'Number-1\.(\d+) (?:times|multiplied by) Number-1\.(\d+)',
        r'The product of Number-1\.(\d+) and Number-1\.(\d+)',
        r'Multiply Number-1\.(\d+) by Number-1\.(\d+)',
    ]
    for pattern in mul_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('mul', int(match.group(1)), int(match.group(2)))
    
    # Division patterns
    div_patterns = [
        r'Number-1\.(\d+) (?:divided by|over) Number-1\.(\d+)',
    ]
    for pattern in div_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('div', int(match.group(1)), int(match.group(2)))
    
    return None

# Parse all formulas
formulas = {}
for req_num, definition in requirements.items():
    formula = parse_definition(definition)
    if formula:
        formulas[req_num] = formula
    else:
        print(f"Warning: Could not parse requirement 1.{req_num}: {definition}")

print(f"Parsed {len(formulas)} formulas")

# Evaluate the formulas recursively
cache = {}

def evaluate(num):
    """Evaluate Number-1.num recursively."""
    if num in cache:
        return cache[num]
    
    if num not in formulas:
        raise ValueError(f"Number-1.{num} not found in formulas")
    
    formula = formulas[num]
    
    if formula[0] == 'const':
        result = formula[1]
    elif formula[0] == 'add':
        result = evaluate(formula[1]) + evaluate(formula[2])
    elif formula[0] == 'sub':
        result = evaluate(formula[1]) - evaluate(formula[2])
    elif formula[0] == 'mul':
        result = evaluate(formula[1]) * evaluate(formula[2])
    elif formula[0] == 'div':
        result = evaluate(formula[1]) / evaluate(formula[2])
    else:
        raise ValueError(f"Unknown operation: {formula[0]}")
    
    cache[num] = result
    return result

# Calculate the secret number (Number-1.1)
secret_number = evaluate(1)

print(f"\nSecret Number (Number-1.1): {secret_number}")
print(f"As integer: {int(secret_number)}")
