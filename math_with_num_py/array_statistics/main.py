import numpy as np
# Simulated test scores of 2 students for five different exams
exam_scores = np.array([[85, 90, 78, 92, 88], [72, 89, 65, 78, 92]])
# Calculate the mean score for each student
mean_scores = np.mean(exam_scores, axis=1)
print(f'Mean score for each student: {mean_scores}')
# Calculate the median score of all scores
median_score = np.median(exam_scores)
print(f'Median score for all scores: {median_score}')
# Calculate the variance of all scores
scores_variance = np.var(exam_scores)
print(f'Variance for all scores: {scores_variance}')
# Calculate the standard deviation of all scores
scores_std = np.std(exam_scores)
print(f'Standard deviation for all scores: {scores_std}')