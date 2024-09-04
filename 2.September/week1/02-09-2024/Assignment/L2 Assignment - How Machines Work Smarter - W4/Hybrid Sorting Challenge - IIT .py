def solve(nums):
    n = len(nums)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    print(" ".join(map(str, nums)))


