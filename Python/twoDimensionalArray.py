import numpy as np

# Day 1 - 11,15,10,6
# Day 2 - 10,24,11,5
# Day 3 - 12,17,12,8
# Day 4 - 15,18,14,9 

week_data = np.array([[11,15,10,6],[10,24,11,5],[12,17,12,8],[15,18,14,9]])
print(week_data)

# Append a column value
""" Insert and append methods """
new_week = np.insert(week_data, len(week_data), [[3,6,9,2]], axis=1)
print("\n ", new_week)

new_week = np.append(week_data, [[3], [6],[9],[2]], axis=1)
print("\n ", new_week)


# Append a row value
""" Insert and append methods """
new_week = np.insert(week_data, 0, [[47,12,34,2]], axis=0)
print("\n ", new_week)

new_week = np.append(week_data, [[1,2,3,4]], axis=0)
print("\n ", new_week)