def stairs(x):
    # Handle edge cases
    if x == 0:
        # If there are 0 steps, there is exactly 1 way to stay at the ground level
        return 1
    if x == 1:
        # If there is 1 step, there is exactly 1 way to reach the first step
        return 1
    
    # Initialize an array to store the number of ways to reach each step
    # The size of the array is (x + 1) to accommodate steps from 0 to x
    ways = [0] * (x + 1)
    
    # Base cases
    ways[0] = 1  # There is 1 way to stay at the ground level (step 0)
    ways[1] = 1  # There is 1 way to reach the first step (step 1)
    
    # Compute the number of ways to reach each step from 2 to x
    for i in range(2, x + 1):
        # The number of ways to reach step 'i' is the sum of the ways to reach
        # the previous step 'i - 1' and the step before that 'i - 2'
        ways[i] = ways[i - 1] + ways[i - 2]
    
    # Return the number of ways to reach the x-th step
    return ways[x]

# Example usage:
# print(stairs(5))  # This will print the number of ways to climb 5 steps
