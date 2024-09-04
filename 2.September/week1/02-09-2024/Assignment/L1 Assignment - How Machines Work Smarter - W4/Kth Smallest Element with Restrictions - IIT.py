def solve(n, nums, k):
    # Implementing a simple selection algorithm to find the kth smallest element
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the found minimum element with the element at index i
        nums[i], nums[min_index] = nums[min_index], nums[i]
    
    # The kth smallest element is now at index k-1
    print(nums[k-1])