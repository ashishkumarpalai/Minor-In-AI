def print_diamond(n):
    # Print the top part of the diamond
    for i in range(n):
        # Calculate the number of leading spaces needed for alignment
        # For each row 'i', we need (n - i - 1) spaces
        # This centers the stars as 'i' increases
        spaces = ' ' * (n - i - 1)
        
        # Calculate the number of stars for the current row
        # For each row 'i', the number of stars is (2 * i + 1)
        # This ensures that the number of stars increases as 'i' increases
        stars = '*' * (2 * i + 1)
        
        # Print the current row with spaces and stars
        print(spaces + stars)
    
    # Print the bottom part of the diamond
    for i in range(n - 2, -1, -1):
        # Calculate the number of leading spaces needed for alignment
        # For each row 'i', we need (n - i - 1) spaces
        # This centers the stars as 'i' decreases
        spaces = ' ' * (n - i - 1)
        
        # Calculate the number of stars for the current row
        # For each row 'i', the number of stars is (2 * i + 1)
        # This ensures that the number of stars decreases as 'i' decreases
        stars = '*' * (2 * i + 1)
        
        # Print the current row with spaces and stars
        print(spaces + stars)

# Example usage to print a diamond with 5 rows
# print_diamond(5)
