def highest_salary_per_employee(employees_salaries):
    # Create a new dictionary to store the highest salary for each employee
    highest_salary_dict = {}
    
    # Iterate over each employee and their list of salaries
    for employee, salaries in employees_salaries.items():
        # 'employee' is the name of the employee
        # 'salaries' is a list of that employee's salaries
        
        # Find the highest salary for the current employee
        # 'max(salaries)' returns the largest value in the list of salaries
        highest_salary_dict[employee] = max(salaries)
    
    # Return the dictionary with the highest salaries
    # The dictionary 'highest_salary_dict' now maps each employee to their highest salary
    return highest_salary_dict
