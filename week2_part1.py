from itertools import combinations
from tqdm import tqdm

#with open('example_week2_part1.txt', 'r') as file:
with open('2.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = {int(k): int(v) for k, v in (line.split(' -> ') for line in data)}
    print(data)
def number_to_bit(num, padding=0) -> list:
    """Convert a number to its binary representation as a list of bits.

    Args:
        num (int): The number to convert.
        padding (int): The minimum number of bits to return (will pad with leading zeros).
    Returns:
        list: A list of bits representing the binary form of the number.
    """    
    bits = [int(bit) for bit in bin(num)[2:]]
    while len(bits) < padding:
        bits.insert(0, 0)
    return bits

def bit_to_number(bits) -> int:
    """Convert a list of bits to its corresponding number.

    Args:
        bits (list): A list of bits (0s and 1s).
    Returns:
        int: The number represented by the bits.
    """    
    return sum(bit * (2 ** idx) for idx, bit in enumerate(reversed(bits)))

def find_correct_answer(guesses:dict) -> int:
    """Find the correct answer given guesses and their hamming distances.
    
    Args:
        guesses (dict): A dict where keys are guessed numbers and values are 
                        hamming distances from the correct answer.
    Returns:
        int: The correct answer.
    """
    # Convert to binary with enough padding
    max_num = max(guesses.keys())
    bit_length = len(bin(max_num)[2:])
    
    # Sort guesses by hamming distance (ascending)
    sorted_guesses = sorted(guesses.items(), key=lambda x: x[1])
    
    result_set = None
    
    for guess_num, hamming_dist in tqdm(sorted_guesses, desc="Processing guesses"):
        print(f"\nProcessing guess {guess_num} with hamming distance {hamming_dist}")
        
        # Convert guess to bits
        guess_bits = number_to_bit(guess_num, bit_length)
        
        if result_set is None:
            # First guess: generate all candidates
            result_set = {
                bit_to_number([1 - guess_bits[i] if i in positions else guess_bits[i] 
                              for i in range(bit_length)])
                for positions in combinations(range(bit_length), hamming_dist)
            }
            print(f"Generated {len(result_set)} initial candidates")
        else:
            # For subsequent guesses: filter existing candidates
            filtered_set = set()
            for candidate in result_set:
                candidate_bits = number_to_bit(candidate, bit_length)
                # Calculate hamming distance between candidate and current guess
                dist = sum(1 for i in range(bit_length) if candidate_bits[i] != guess_bits[i])
                if dist == hamming_dist:
                    filtered_set.add(candidate)
            result_set = filtered_set
            print(f"After filtering, {len(result_set)} candidates remain")
    
    print(f"\nFinal result set: {result_set}")
    
    if len(result_set) == 1:
        return result_set.pop()
    else:
        raise ValueError(f"Expected 1 solution, found {len(result_set)}")


correct_answer = find_correct_answer(data)
print(f"The correct answer is: {correct_answer}")