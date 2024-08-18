def vigenere_encrypt(plaintext, key):
    # Define the alphabet used for encryption
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Initialize an empty list to store the encrypted characters
    encrypted_text = []
    
    # Convert both plaintext and key to uppercase to ensure consistency
    plaintext = plaintext.upper()
    key = key.replace(" ", "").upper()  # Also, remove any spaces in the key
    
    # Initialize an index to keep track of the current position in the key
    key_index = 0
    
    # Loop through each character in the plaintext
    for char in plaintext:
        if char in alphabet:
            # If the character is in the alphabet, perform encryption
            
            # Get the corresponding character from the key based on the current key index
            key_char = key[key_index % len(key)]
            
            # Find the shift value, which is the index of the key character in the alphabet
            shift = alphabet.index(key_char)
            
            # Encrypt the plaintext character by shifting it forward by the shift value
            encrypted_char = alphabet[(alphabet.index(char) + shift) % 26]
            
            # Append the encrypted character to the list
            encrypted_text.append(encrypted_char)
            
            # Move to the next character in the key by incrementing the key index
            key_index += 1
        else:
            # If the character is not in the alphabet (e.g., space or punctuation), append it unchanged
            encrypted_text.append(char)
    
    # Join the list of encrypted characters into a single string and return it
    return ''.join(encrypted_text)
