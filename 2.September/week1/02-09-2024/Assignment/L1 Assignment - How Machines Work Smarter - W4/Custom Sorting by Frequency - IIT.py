def solve(n, nums):
    # Step 1: Count the frequency of each number
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Step 2: Define a custom function for sorting
    def custom_sort(x):
        return (frequency[x], nums.index(x))
    
    # Step 3: Sort the list using the custom function as the key
    sorted_nums = sorted(nums, key=custom_sort)
    
    # Step 4: Print the result with space-separated elements
    print(" ".join(map(str, sorted_nums)))

