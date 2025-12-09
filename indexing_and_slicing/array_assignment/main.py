import numpy as np
# Employee data: each row represents an employee [salary, performance_score]
employee_data = np.array([[4500, 7], [3800, 8], [5200, 9], [4700, 6], [4300, 7], [3900, 5]])
# Assign 6000 to the salary of the fourth employee
employee_data[3, 0] = 6000
print(employee_data)