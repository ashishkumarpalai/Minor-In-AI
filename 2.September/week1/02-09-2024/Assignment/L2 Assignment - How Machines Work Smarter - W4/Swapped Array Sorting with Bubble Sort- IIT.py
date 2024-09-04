def solve(nums):
    n = len(nums)
    for i in range(n):
        # Track if any swapping happens
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                # Swap if the element found is greater
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        # If no swapping happened, the list is already sorted
        if not swapped:
            break
    # print(nums)
    print(" ".join(map(str, nums)))
