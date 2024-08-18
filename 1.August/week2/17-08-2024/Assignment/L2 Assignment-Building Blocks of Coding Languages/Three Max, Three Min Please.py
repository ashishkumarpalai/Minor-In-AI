def solve(N, arr):
    # This is the main function that takes two inputs:
    # N: the number of elements in the array
    # arr: a list of integers

    # Convert the list `arr` to a set to remove any duplicate values
    arr = set(arr)
    
    # Sort the unique elements in ascending order and convert the set back to a list
    arr = sorted(arr)
    
    # Check if the length of the sorted list is less than 3
    if len(arr) < 3:
        # If there are fewer than 3 unique elements, print "Not Possible" twice
        print("Not Possible")
        print("Not Possible")
        # Return from the function as no further processing is possible
        return
    
    # If there are at least 3 unique elements, print the first 3 smallest elements
    print(" ".join(str(x) for x in arr[:3]))
    
    # Print the last 3 largest elements from the sorted list
    print(" ".join(str(x) for x in arr[-3:]))
