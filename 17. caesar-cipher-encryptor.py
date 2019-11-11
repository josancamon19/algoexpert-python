def encode_char(char, key):
    # [ 97 - 122 ] --> [ a - z ]
    return str(chr(97 + (((ord(char) + key) - 97) % 26)))


def caesarCipherEncryptor(string, key):
    # Write your code here.
    return ''.join([encode_char(char, key) for char in string])


if __name__ == '__main__':
    print(caesarCipherEncryptor('abc', 52))
