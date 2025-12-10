import numpy as np
# Simulated quarterly sales data for two products in 2021
sales_data_2021 = np.array([[350, 420, 380, 410], [270, 320, 290, 310]])
# Create a copy of sales_data_2021
sales_data_2022 = sales_data_2021.copy()
# Assign the NumPy array with elements 390 and 370 to the correct slice 
sales_data_2022[0, -2:] = np.array([390, 370])
print(f'Quarterly sales in 2021:\n{sales_data_2021}')
print(f'Quarterly sales in 2022:\n{sales_data_2022}')