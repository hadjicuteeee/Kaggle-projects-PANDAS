import pandas as pd

students_2024 = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Anna', 'Ben', 'Carla']
})

students_2025 = pd.DataFrame({
    'student_id': [2, 3, 4],
    'name': ['Ben', 'Carla', 'Daniel']
})

only_2024 = students_2024.merge(students_2025, on=['student_id', 'name'], how='left', indicator=True)
only_2024 = only_2024[only_2024['_merge'] == 'left_only']
only_2024 = only_2024.drop(columns=['_merge'])

print(only_2024)
