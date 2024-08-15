def magical_words(word_list):
    
    # Find the Word with the Most Vowels
    vowels_count = []
    for word in word_list:
        count = 0
        for char in word:
            if char.lower() in "aeiou":
                count += 1
        vowels_count.append((count, word))
    
    vowels_count.sort()
    
    max_count = 0
    for count, word in vowels_count:
        if max_count < count:
            max_count = count

    for count, word in vowels_count:
        if count == max_count and word.isupper():
            print("Highest Vowels:", word)
            break
        elif count == max_count:
            print("Highest Vowels:", word)
            break
        
    # Identify Palindrome Words
    palindrome_word_list = []
    for word in word_list:
        if word.lower() == word[::-1].lower():
            palindrome_word_list.append(word)
  
    # Print the palindromes as a comma-separated list
    if palindrome_word_list:
        print("Palindrome:", ", ".join(palindrome_word_list))
    else:
        print("Palindrome: None")
    
    # Count Duplicate Words (case-insensitive)
    duplicate_word_dict = {}
    for word in word_list:
        word_lower = word.lower()
        if word_lower in duplicate_word_dict:
            duplicate_word_dict[word_lower] += 1
        else:
            duplicate_word_dict[word_lower] = 1
    
    duplicate_word_list = []
    for word, count in duplicate_word_dict.items():
        if count > 1:
            duplicate_word_list.append(word)
    
    # Print duplicates as a comma-separated list
    if duplicate_word_list:
        print("Duplicate Words:", ", ".join(duplicate_word_list))
    else:
        print("Duplicate Words: None")











# def magical_words(word_list):
#     '''
#     Analyze the given list of words to:
#     1. Find the word with the most vowels.
#     2. Identify palindrome words.
#     3. Count duplicate words.
#     '''

#     # Function to count vowels in a word
#     def count_vowels(word):
#         return sum(1 for char in word.lower() if char in 'aeiou')

#     # Convert all words to lowercase for case-insensitive comparison
#     words_lower = [word.lower() for word in word_list]
    
#     # Track the maximum number of vowels and corresponding words
#     max_vowels = 0
#     max_vowel_words = []
    
#     # Track palindromes
#     palindromes = []
    
#     # Count occurrences of each word (case-insensitive)
#     from collections import Counter
#     word_counts = Counter(words_lower)
    
#     # Track duplicate words
#     duplicate_words = set()

#     # Analyze each word in the input list
#     for word in word_list:
#         word_lower = word.lower()
        
#         # Update max vowel words
#         num_vowels = count_vowels(word)
#         if num_vowels > max_vowels:
#             max_vowels = num_vowels
#             max_vowel_words = [word]
#         elif num_vowels == max_vowels:
#             max_vowel_words.append(word)
        
#         # Check if the word is a palindrome
#         if word_lower == word_lower[::-1]:
#             palindromes.append(word)
        
#         # Track duplicate words
#         if word_counts[word_lower] > 1:
#             duplicate_words.add(word_lower)

#     # Prepare outputs for highest vowels
#     if max_vowel_words:
#         # Convert to uppercase if the word is originally uppercase
#         highest_vowels_word = min(max_vowel_words, key=lambda w: (w.lower(), w))
#     else:
#         highest_vowels_word = "None"

#     palindromes_output = ", ".join(palindromes) if palindromes else "None"
#     duplicate_words_output = ", ".join(sorted(set(word_list[i].lower() for i in range(len(word_list)) if word_counts[word_list[i].lower()] > 1))) if duplicate_words else "None"
    
#     # Print results
#     print(f"Highest Vowels: {highest_vowels_word}")
#     print(f"Palindrome: {palindromes_output}")
#     print(f"Duplicate Words: {duplicate_words_output}")


