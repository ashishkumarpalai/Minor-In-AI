def solve(n, nums, x):
    # Create a list of tuples where each tuple is (absolute_difference, original_index, original_value)
    diff_list = []
    for i in range(n):
        abs_diff = abs(nums[i] - x)
        diff_list.append((abs_diff, i, nums[i]))

    # Sort the list of tuples primarily by absolute_difference, and by original_index if there's a tie
    diff_list.sort()

    # Extract the sorted values
    sorted_nums = [tup[2] for tup in diff_list]

    # Print the sorted list with elements separated by spaces
    print(" ".join(map(str, sorted_nums)))


