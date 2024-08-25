def is_palindrome(word):
    # Convert the word to lowercase to make the palindrome check case-insensitive
    cleaned_word = word.lower()
    # Check if the cleaned word reads the same forwards and backwards
    # cleaned_word[::-1] reverses the string
    return cleaned_word == cleaned_word[::-1]

def palindrome_dictionary(sentences):
    # Initialize an empty dictionary to store results
    result = {}
    
    # Iterate over each sentence in the list
    for sentence in sentences:
        # Split the sentence into words based on spaces
        words = sentence.split()
        # Initialize the count of palindromic words to 0
        palindrome_count = 0
        
        # Iterate over each word in the list of words
        for word in words:
            # Remove non-alphanumeric characters from the word
            # ''.join(char for char in word if char.isalnum()) creates a new string with only alphanumeric characters
            cleaned_word = ''.join(char for char in word if char.isalnum())
            # Check if the cleaned word is a palindrome
            if is_palindrome(cleaned_word):
                # Increment the palindrome count if the word is a palindrome
                palindrome_count += 1
        
        # Add the sentence and its corresponding palindrome count to the dictionary
        result[sentence] = palindrome_count
    
    # Return the dictionary with sentences and their palindrome counts
    return result
