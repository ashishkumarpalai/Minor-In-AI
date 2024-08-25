def concatenate_array(nums):
    # Concatenate the list with itself
    return nums * 2

# Read the number of elements from user input
n = int(input())

if n != 0:
    # Read the list of numbers from user input
    nums = list(map(int, input().split()))
    # Get the concatenated result by calling the function
    result = concatenate_array(nums)
    # Print the result, unpacking the list elements so they are printed separately
    print(*result)
else:
    # If the number of elements is 0, print an empty line
    print()
