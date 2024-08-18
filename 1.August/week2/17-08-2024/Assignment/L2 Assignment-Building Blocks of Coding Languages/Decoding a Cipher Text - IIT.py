def decode_ciphertext(ciphertext, key):
    # This function decodes an encrypted message using a provided substitution key.
    # 'ciphertext' is the encrypted message, and 'key' is the string that represents
    # how each letter in the alphabet has been substituted.

    # The standard alphabet to map against
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Create a dictionary (key_mapping) to map each letter in the key to the corresponding letter in the alphabet
    key_mapping = {key[i]: alphabet[i] for i in range(len(alphabet))}
    # Explanation:
    # - key[i]: Refers to the character in the key at position 'i'.
    # - alphabet[i]: Refers to the corresponding character in the alphabet at position 'i'.
    # This creates a dictionary where each letter in the key is associated with a letter in the standard alphabet.

    # Initialize an empty list to hold the decoded message
    decoded_message = []
    
    # Loop through each character in the ciphertext
    for char in ciphertext:
        if char in key_mapping:
            # If the character is found in the key_mapping dictionary, append the corresponding
            # letter from the alphabet to the decoded_message list.
            decoded_message.append(key_mapping[char])
        else:
            # If the character is not in the key_mapping (e.g., spaces, punctuation),
            # add it directly to the decoded_message list without any change.
            decoded_message.append(char)
    
    # Join the list of characters into a single string and print the decoded message
    print(''.join(decoded_message))
