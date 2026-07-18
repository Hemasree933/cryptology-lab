def vigenere_encrypt(text, key):
    result = []
    key = key.upper()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


def vigenere_decrypt(text, key):
    result = []
    key = key.upper()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


# Example usage
message = "HELLO WORLD"
key = "KEY"

encrypted = vigenere_encrypt(message, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)



