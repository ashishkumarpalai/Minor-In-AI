def is_leap_year(date_string):
    # Extract the year from the date string
    year = int(date_string[:4])
    
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
