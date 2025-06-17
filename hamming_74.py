def hamming_encode(data):
    """Encode 4-bit data to 7-bit Hamming code"""
    d = [int(b) for b in data]
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p4 = d[1] ^ d[2] ^ d[3]
    return f"{p1}{p2}{d[0]}{p4}{d[1]}{d[2]}{d[3]}"


def hamming_decode(received):
    """Decode and correct 7-bit Hamming code with 2-bit error detection"""
    r = [int(b) for b in received]
    # Calculate syndrome bits
    s1, s2, s3 = (
        r[0] ^ r[2] ^ r[4] ^ r[6],
        r[1] ^ r[2] ^ r[5] ^ r[6],
        r[3] ^ r[4] ^ r[5] ^ r[6],
    )
    # Calculate overall parity (should be 0 for valid codeword)
    parity = sum(r) % 2
    syndrome = s1 + 2 * s2 + 4 * s3

    decoded = f"{r[2]}{r[4]}{r[5]}{r[6]}"
    if syndrome == 0 and parity == 0:
        return decoded, "No error detected"
    elif syndrome != 0 and parity == 1:
        print(f"Single error at position {syndrome}")
        r[syndrome - 1] ^= 1  # flip bit
        return decoded, "Single error corrected"
    else:  # syndrome != 0 and parity == 0
        return decoded, "Double error detected (cannot correct)"


# Main program
send_data = input("Enter 4-bit data to send: ")
encoded = hamming_encode(send_data)
print(f"Encoded (7,4) Hamming code: {encoded}")

received_data = input("Enter received 7-bit code: ")
decoded, status = hamming_decode(received_data)
print(f"Decoded data: {decoded}")
print(f"Status: {status}")
