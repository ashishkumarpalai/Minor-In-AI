def string_score(s):
    # Initialize the total score to 0
    total_score = 0
    
    # Iterate through the string from the start to the second-to-last character
    for i in range(len(s) - 1):
        # Calculate the absolute difference between the ASCII values of adjacent characters
        diff = abs(ord(s[i]) - ord(s[i + 1]))
        # Add the difference to the total score
        total_score += diff
    
    # Return the total score
    return total_score
