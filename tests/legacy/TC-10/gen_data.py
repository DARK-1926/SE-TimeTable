import pandas as pd
courses = []
for i in range(60):
    courses.append(['CSE', 2, f'CS90{i}', f'Stress Test {i}', 3, 1, 0, 0, 4, f'Fac {i}', 'YES', 50, 'ALL', 'COMBINED', '', ''])

df = pd.DataFrame(courses, columns=['Department','Semester','Course Code','Course Name','L','T','P','S','C','Faculty','Schedule','total_students','Section','SectionMode','CrossDeptGroup','CrossDeptMode'])
df.to_csv(r'c:\Users\mohit\Downloads\SE TT\Automated-Time-Table-Scheduling-at-IIIT-Dharwad\tests\TC-10\data\combined_even.csv', index=False)
