def solve(N):
    # This function calculates the factorial of a given number N.
    # N is expected to be a non-negative integer.
    
    fact = 1
    # Initialize a variable `fact` to 1. This will hold the result of the factorial calculation.
    
    for i in range(1, N + 1):
        # Start a loop from 1 to N (inclusive). The loop variable `i` will take each integer value in this range.
        
        fact *= i
        # Multiply the current value of `fact` by `i` and store the result back into `fact`.
        # This effectively calculates the product of all integers from 1 to N.
    
    print(fact)
    # After the loop completes, print the value of `fact`, which now contains the factorial of N.
