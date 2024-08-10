def calculate_median(scores):
    # Step 1: Sort the list of scores
    scores.sort()

    # Step 2: Find the number of scores
    n = len(scores)

    # Step 3: Calculate the median
    if n % 2 == 1:
        # If the number of scores is odd, the median is the middle value
        median = scores[n // 2]
    else:
        # If the number of scores is even, the median is the average of the two middle values
        middle1 = scores[n // 2 - 1]
        middle2 = scores[n // 2]
        median = (middle1 + middle2) / 2

    return median
