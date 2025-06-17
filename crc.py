def xor_divide(dividend, divisor):
    """Perform XOR division and return remainder"""
    dividend = list(dividend)  # Convert to list for easy modification

    for i in range(len(dividend) - len(divisor) + 1):  # can divide this many times
        if dividend[i] == "1":  # Only divide when leading bit is 1
            # XOR each bit of divisor with corresponding bits in dividend
            for j in range(len(divisor)):
                dividend[i + j] = str(int(dividend[i + j]) ^ int(divisor[j]))

    # Return the remainder (last few bits)
    return "".join(dividend[-(len(divisor) - 1) :])


def crc_encode(data, generator):
    """Generate CRC codeword"""
    # Step 1: Append zeros equal to (generator length - 1)
    padded_data = data + "0" * (len(generator) - 1)
    print(f"Padded data: {padded_data}")

    # Step 2: Perform XOR division
    remainder = xor_divide(padded_data, generator)
    print(f"CRC remainder: {remainder}")

    # Step 3: Replace appended zeros with remainder
    codeword = data + remainder
    return codeword


def crc_check(received_data, generator):
    """Check if received data has errors"""
    print(f"Checking: {received_data}")

    # Perform XOR division on received data
    remainder = xor_divide(received_data, generator)
    print(f"Division remainder: {remainder}")

    # If remainder is all zeros, no error
    if remainder == "0" * (len(generator) - 1):
        return "No Error Detected"
    else:
        return "Error Detected"


# Main program
print("=== CRC Generator ===")
data_bits = input("Enter data bits: ")
generator_poly = input("Enter generator polynomial: ")

print(f"\nEncoding '{data_bits}' with generator '{generator_poly}':")
codeword = crc_encode(data_bits, generator_poly)
print(f"Final codeword: {codeword}")

print("\n=== Error Checking ===")
received_codeword = input("Enter received codeword: ")
result = crc_check(received_codeword, generator_poly)
print(f"Result: {result}")
