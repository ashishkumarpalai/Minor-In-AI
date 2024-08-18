def factors(n):
    '''
    This function returns a list of all factors of the integer `n`.
    '''
    # Initialize an empty list to store the factors
    factor = []
    
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if `i` is a factor of `n` (i.e., `n % i == 0`)
        # and ensure `i` is greater than 0 (though all `i` in the range will be > 0)
        if n % i == 0:
            # Append the factor to the list
            factor.append(i)
    
    # Return the list of factors
    return factor
def common_factors(a, b):
    '''
    This function returns a list of common factors of integers `a` and `b`.
    '''
    # Initialize an empty list to store the common factors
    complete = []
    
    # Loop through all numbers from 1 to the maximum of `a` and `b` (inclusive)
    for i in range(1, max(a, b) + 1):
        # Check if `i` is a factor of both `a` and `b`
        if a % i == 0 and b % i == 0:
            # Append the common factor to the list
            complete.append(i)
    
    # Return the list of common factors
    return complete
def factors_upto(n):
    '''
    This function returns a dictionary where the keys are integers from 1 to `n`,
    and the values are lists of factors for each integer.
    '''
    # Initialize an empty dictionary to store the factors of each integer
    obj = {}
    
    # Loop through all numbers from 1 to `n` (inclusive)
    for i in range(1, n + 1):
        # Calculate the factors of `i` and store them in the dictionary with key `i`
        obj[i] = factors(i)
    
    # Return the dictionary
    return obj
