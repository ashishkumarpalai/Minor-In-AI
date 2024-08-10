def is_palindrome(sentence):
    # Initialize an empty string to store the cleaned sentence
    cleaned_sentence = ''
    
    # Traverse through the sentence
    for char in sentence:
        # Check if the character is alphanumeric
        if char.isalnum():
            # Convert to lowercase and add to the cleaned sentence
            cleaned_sentence += char.lower()
    
    # Check if the cleaned sentence is equal to its reverse
    if cleaned_sentence == cleaned_sentence[::-1]:
        return "YES"
    else:
        return "NO"
