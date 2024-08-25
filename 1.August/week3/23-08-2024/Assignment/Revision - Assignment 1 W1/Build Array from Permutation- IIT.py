def build_arrays(nums):
    # Initialize the result array with an empty list
    ans = []
    
    # Loop through each index in the nums array
    for i in range(len(nums)):
        # Append the value from nums[nums[i]] to the result array
        # This means we access the value at the index nums[i] in the nums array
        ans.append(nums[nums[i]])
    
    # Return the populated result array
    return ans
