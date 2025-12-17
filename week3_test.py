import re

# Parse the specification and build a dependency graph
requirements = {}

spec_text = """
Requirement 1.1: Test Secret Number
Compute Number-1.15 minus Number-1.4; the difference between these quantities
as defined by Requirements 1.15 and 1.4.
Requirement 1.2: Lower Threshold
Set to -82232; a fixed negative constant.
Requirement 1.3: Net Adjustment
Calculate Number-1.6 minus Number-1.8; subtract Number-1.8 from Number-1.6
per Requirements 1.6 and 1.8.
Requirement 1.4: Offset Plus Delta
Sum Number-1.7 and Number-1.16; Number-1.7 added to Number-1.16, as
specified in Requirements 1.7 and 1.16.
Requirement 1.5: Error Magnitude
Equals -98499; a fixed negative constant.
Requirement 1.6: Residual Baseline
Defined as -80328; a fixed negative baseline value.
Requirement 1.7: Drift Term
Recorded as -61773; a constant representing drift.
Requirement 1.8: Suppression Floor
Assigned -80388; a fixed lower floor constant.
Requirement 1.9: Baseline Delta
Compute Number-1.2 minus Number-1.14; subtract Number-1.14 from Number1.2 per Requirements 1.2 and 1.14.
Requirement 1.10: Raw Measurement
Set to 39024; a fixed positive constant.
Requirement 1.11: Baseline Decrement
Equals -59640; a fixed negative constant.
Requirement 1.12: Normalized Reading
Divide Number-1.10 by Number-1.13; the quotient of these values, as defined in
Requirements 1.10 and 1.13.
Requirement 1.13: Scaling Factor
Exactly 3; a fixed positive multiplier constant.
Requirement 1.14: Adjusted Sum
Add Number-1.5 to Number-1.12; the addition of these two values, per Requirements 1.5 and 1.12.
Requirement 1.15: Ratio of Baselines
Compute Number-1.11 divided by Number-1.3; the result of Number-1.11 over
Number-1.3, as referenced in Requirements 1.11 and 1.3.
Requirement 1.16: Calibration Offset
Set to 58754; a fixed positive offset constant.
"""

# Parse each requirement
lines = spec_text.strip().split('\n')
i = 0
current_req = None
current_def = []

while i < len(lines):
    line = lines[i].strip()
    if line.startswith('Requirement 1.'):
        # Save previous requirement if exists
        if current_req is not None and current_def:
            requirements[current_req] = ' '.join(current_def)
        
        # Extract requirement number
        match = re.match(r'Requirement 1\.(\d+):', line)
        if match:
            current_req = int(match.group(1))
            current_def = []
            # Get text after the colon
            rest = line.split(':', 1)[1].strip()
            if rest:
                current_def.append(rest)
    elif current_req is not None and line:
        # Continue adding to current definition
        current_def.append(line)
    i += 1

# Don't forget the last requirement
if current_req is not None and current_def:
    requirements[current_req] = ' '.join(current_def)

print(f"Parsed {len(requirements)} requirements")
for req_num, definition in sorted(requirements.items()):
    print(f"1.{req_num}: {definition[:60]}...")

# Now parse each definition to extract the formula
def parse_definition(definition):
    """Parse a requirement definition and return a formula."""
    
    # Check for constant - multiple patterns
    const_patterns = [
        r'Set to (-?\d+)',
        r'Equals (-?\d+)',
        r'Defined as (-?\d+)',
        r'Recorded as (-?\d+)',
        r'Assigned (-?\d+)',
        r'Exactly (\d+)',
    ]
    for pattern in const_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('const', int(match.group(1)))
    
    # Check for operations
    # Addition patterns
    add_patterns = [
        r'Sum Number-1\.(\d+) and Number-1\.(\d+)',
        r'Number-1\.(\d+) added to Number-1\.(\d+)',
        r'Add Number-1\.(\d+) to Number-1\.(\d+)',
    ]
    for pattern in add_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('add', int(match.group(1)), int(match.group(2)))
    
    # Subtraction patterns
    sub_patterns = [
        r'Compute Number-1\.(\d+) minus Number-1\.(\d+)',
        r'Number-1\.(\d+) minus Number-1\.(\d+)',
        r'Calculate Number-1\.(\d+) minus Number-1\.(\d+)',
        r'subtract Number-1\.(\d+) from Number-1\.(\d+)',
    ]
    for pattern in sub_patterns:
        match = re.search(pattern, definition)
        if match:
            return ('sub', int(match.group(1)), int(match.group(2)))
    
    # Division patterns
    div_patterns = [
        r'Divide Number-1\.(\d+) by Number-1\.(\d+)',
        r'Number-1\.(\d+) divided by Number-1\.(\d+)',
        r'Number-1\.(\d+) over Number-1\.(\d+)',
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
        print(f"Formula 1.{req_num}: {formula}")
    else:
        print(f"Warning: Could not parse requirement 1.{req_num}: {definition}")

print(f"\nParsed {len(formulas)} formulas")

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
    print(f"Number-1.{num} = {result}")
    return result

# Calculate the secret number (Number-1.1)
print("\n=== Calculating Secret Number ===")
secret_number = evaluate(1)

print(f"\nTest Secret Number (Number-1.1): {secret_number}")
print(f"As integer: {int(secret_number)}")
print(f"\nExpected: 2025")
print(f"Match: {int(secret_number) == 2025}")
