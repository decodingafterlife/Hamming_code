# GitHub: decodingafterlife 
# Tanmay Shingavi
def calculate_parity_bits(data):
    """Calculate the number of parity bits needed."""
    for i in range(10):  # 10 is more than enough for 8-bit data
        if 2**i >= len(data) + i + 1:
            return i

def insert_parity_bits(data):
    """Insert parity bits into the data."""
    m = len(data)
    r = calculate_parity_bits(data)
    result = ['0'] * (m + r)
    j = 0
    for i in range(1, m + r + 1):
        if i & (i - 1) != 0:  # If i is not a power of 2
            result[i-1] = data[j]
            j += 1
    return ''.join(result)

def calculate_hamming_code(data):
    """Calculate Hamming code for given data."""
    encoded = insert_parity_bits(data)
    for i in range(len(encoded)):
        if i & (i + 1) == 0:  # If i+1 is a power of 2
            parity = 0
            for j in range(i + 1, len(encoded) + 1):
                if j & (i + 1) != 0:
                    parity ^= int(encoded[j-1])
            encoded = encoded[:i] + str(parity) + encoded[i+1:]
    return encoded

def ascii_to_hamming(char):
    """Convert an ASCII character to its Hamming code representation."""
    ascii_value = ord(char)
    binary = format(ascii_value, '08b')
    return calculate_hamming_code(binary)

def string_to_hamming(text):
    """Convert a string to Hamming code representation."""
    return [ascii_to_hamming(char) for char in text]

# Example usage
text = "Hello"
hamming_codes = string_to_hamming(text)
for char, code in zip(text, hamming_codes):
    print(f"'{char}' (ASCII {ord(char)}, Binary {format(ord(char), '08b')}) -> Hamming code: {code}")
