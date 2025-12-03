import numpy as np
# Scores of three students in three subjects
student_scores = np.array([[85, 92, 78], [88, 75, 83], [90, 88, 91]])
# Create a slice of student_scores with the scores of the first student in the last two subjects
first_student_last_two_scores = student_scores[0, 1:]
print(first_student_last_two_scores)