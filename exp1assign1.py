import numpy as np

#Create a NumPy array containing the internal marks of 10 students
internal_marks = np.array([42, 38, 45, 49, 31, 47, 40, 35, 44, 39])

#Calculate the required statistical values
marks_mean = np.mean(internal_marks)
marks_median = np.median(internal_marks)
marks_std = np.std(internal_marks)
marks_max = np.max(internal_marks)
marks_min = np.min(internal_marks)

# 3. Print the results
print(f"Internal Marks of Students: {internal_marks}")
print(f"Mean Mark:                  {marks_mean}")
print(f"Median Mark:                {marks_median}")
print(f"Standard Deviation:         {marks_std:.2f}")
print(f"Maximum Mark:               {marks_max}")
print(f"Minimum Mark:               {marks_min}")
