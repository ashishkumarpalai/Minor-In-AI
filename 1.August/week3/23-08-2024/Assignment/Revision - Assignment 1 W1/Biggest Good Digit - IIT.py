def biggest_good_digit(num):
    # Check if the input string is empty
    if not num:
        return -1  # Return -1 if there's no input

    # Initialize a dictionary to count occurrences of each digit
    count = {}
    
    # Count the frequency of each digit in the string
    for digit in num:
        if digit in count:
            count[digit] += 1  # Increment count if digit is already in dictionary
        else:
            count[digit] = 1  # Initialize count for new digit
    
    # Initialize variables to find the digit with the highest frequency
    max_freq = 1  # Start with 1 because we're looking for digits that appear more than once
    max_digit = -1  # Default value if no digit is good
    
    # Iterate through the dictionary to find the digit with the highest frequency
    for digit, freq in count.items():
        # Check if the current frequency is greater than the recorded maximum frequency
        if freq > max_freq:
            max_freq = freq  # Update max frequency
            max_digit = int(digit)  # Update the digit with this frequency
        elif freq == max_freq:
            # If the current frequency is equal to the maximum frequency, choose the larger digit
            max_digit = max(max_digit, int(digit))
    
    # Return the largest good digit or -1 if no digit appears more than once
    return max_digit if max_digit != -1 else -1
