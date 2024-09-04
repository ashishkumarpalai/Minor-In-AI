def solve(n, nums):
    # Split the input into positive and non-positive lists
    positive_nums = [num for num in nums if num > 0]
    non_positive_nums = [num for num in nums if num <= 0]
    
    # Sort the positive numbers
    positive_nums.sort()
    
    # Concatenate the sorted positive numbers with the non-positive numbers
    sorted_list = positive_nums + non_positive_nums
    
    # Print the result with space-separated elements
    print(" ".join(map(str, sorted_list)))

