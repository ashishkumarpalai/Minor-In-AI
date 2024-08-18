def find_top_student(students_scores):
    # Complete this function to find the student(s) with the highest score

    # Initialize an empty list to store all the scores
    max_list = []
    
    # Loop through each student in the dictionary `students_scores`
    for i in students_scores:
        # Append the score of each student to `max_list`
        max_list.append(students_scores.get(i))
    
    # Find the maximum score from the `max_list`
    max_num = max(max_list)
    
    # Initialize an empty list to store the name(s) of the top student(s)
    students = []
    
    # Loop through each student in the dictionary again
    for i in students_scores:
        # If the student's score matches the maximum score, add the student's name to `students`
        if students_scores.get(i) == max_num:
            students.append(i)
    
    # If more than one student has the top score, return the list of names
    if len(students) > 1:
        return students
    else:
        # If only one student has the top score, return the name of that student
        return students[0]
