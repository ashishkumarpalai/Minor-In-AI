def calculate_median(scores):
    '''
    This function calculates the median of a list of scores.
    The `scores` list is provided as an input to the function.
    '''
    
    # Sort the list of scores in ascending order
    scores = sorted(scores)
    
    # Initialize a variable `res` to store the median result
    res = 0
    
    # Check if the length of the list `scores` is even
    if len(scores) % 2 == 0:
        # If the list length is even, calculate the median as the average of the two middle elements
        median = len(scores) // 2
        
        # Calculate the average of the middle two elements
        res = (scores[median - 1] + scores[median]) / 2
        
    else:
        # If the list length is odd, the median is the middle element
        median = (len(scores) + 1) // 2
        
        # Get the middle element as the median
        res = scores[median - 1]
    
    # Print the calculated median
    print(res)
