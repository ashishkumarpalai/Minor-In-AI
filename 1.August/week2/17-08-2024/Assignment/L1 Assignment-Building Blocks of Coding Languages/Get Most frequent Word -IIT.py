def get_most_frequent_word(lines):
    # Helper function to clean the text by removing punctuation and converting to lowercase
    def clean_text(text):
        # Initialize an empty list to store characters that will be part of the cleaned text
        cleaned_text = []
        # Iterate over each character in the input text
        for char in text:
            # Include alphanumeric characters and spaces in the cleaned text
            if char.isalnum() or char.isspace():
                cleaned_text.append(char)
        # Join the list of characters into a single string and convert to lowercase
        return ''.join(cleaned_text).lower()
    
    # Helper function to count occurrences of each word in a list of words
    def count_words(words):
        # Initialize an empty dictionary to store word counts
        word_count = {}
        # Iterate over each word in the list of words
        for word in words:
            # Check if the word is not empty
            if word:
                # If the word is already in the dictionary, increment its count
                if word in word_count:
                    word_count[word] += 1
                # Otherwise, add the word to the dictionary with a count of 1
                else:
                    word_count[word] = 1
        # Return the dictionary with word counts
        return word_count
    
    # Check if the list of lines is empty
    if not lines:
        # Return message if no lines are provided
        return "No valid words found in the list."
    
    # Initialize an empty list to collect all words from all lines
    all_words = []
    
    # Process each line in the list
    for line in lines:
        # Clean the line by removing punctuation and converting to lowercase
        cleaned_line = clean_text(line)
        # Split the cleaned line into a list of words
        words = cleaned_line.split()
        # Add the words to the list of all words
        all_words.extend(words)
    
    # Check if there are no valid words after processing
    if not all_words:
        # Return message if no valid words are found
        return "No valid words found in the list."
    
    # Count the occurrences of each word in the list
    word_count = count_words(all_words)
    
    # Initialize variables to find the most frequent word
    most_frequent_word = None
    max_count = 0
    
    # Iterate through the dictionary of word counts
    for word, count in word_count.items():
        # Update the most frequent word if the current word has a higher count
        if count > max_count:
            most_frequent_word = word
            max_count = count
    
    # Check if a most frequent word was found
    if most_frequent_word:
        # Return the most frequent word
        return most_frequent_word
    else:
        # Return message if no valid words are found
        return "No valid words found in the list."
