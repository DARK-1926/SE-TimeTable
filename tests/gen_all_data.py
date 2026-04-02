"""Generate/fix data files for TC-04, TC-11, TC-14, TC-16..TC-20."""
import pandas as pd
import os

def write_rooms(path, rooms):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('id,roomNumber,capacity,type\n')
        for r in rooms:
            f.write(f'{r[0]},{r[1]},{r[2]},{r[3]}\n')

# --- FIX TC-04: 15 unique courses, ALL Schedule=YES ---
courses_04 = []
names = ['Algorithms','Networks','OS','DBMS','AI','ML','Compilers','Graphics',
         'Security','Cloud','Distributed','HCI','Robotics','NLP','Blockchain']
for i, name in enumerate(names):
    courses_04.append({
        'Department':'CSE','Semester':4,'Course Code':f'CS4{i+1:02d}',
        'Course Name':name,'L':3,'T':1,'P':0,'S':0,'C':4,
        'Faculty':'Dr. Overloaded','Schedule':'YES','total_students':50,
        'Section':'ALL','SectionMode':'COMBINED'
    })
pd.DataFrame(courses_04).to_csv('tests/TC-04/data/combined_even.csv', index=False)
print('TC-04 fixed: 15 unique courses, ALL Schedule=YES')

# --- FIX TC-11: 5 cores + B1(3) + B2(2) + B4(1) ---
courses_11 = [
    {'Department':'CSE','Semester':2,'Course Code':'MA163','Course Name':'Linear Algebra',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Anand','Schedule':'YES','total_students':110,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':2,'Course Code':'CS162','Course Name':'Optimization',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Guha','Schedule':'YES','total_students':110,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':2,'Course Code':'CS163','Course Name':'Data Structures',
     'L':3,'T':0,'P':2,'S':0,'C':4,'Faculty':'Dr. Vivekraj','Schedule':'YES','total_students':110,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':2,'Course Code':'CS208','Course Name':'Computer Architecture',
     'L':3,'T':0,'P':2,'S':0,'C':2,'Faculty':'Dr. Prabhu','Schedule':'YES','total_students':110,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':2,'Course Code':'CS201','Course Name':'Discrete Math',
     'L':3,'T':0,'P':0,'S':0,'C':3,'Faculty':'Dr. Hazra','Schedule':'YES','total_students':110,
     'Section':'ALL','SectionMode':'COMBINED'},
    # B1 basket (3 courses)
    {'Department':'CSE','Semester':2,'Course Code':'B1-CS154','Course Name':'Data Analytics',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Abdul','Schedule':'YES','total_students':30},
    {'Department':'CSE','Semester':2,'Course Code':'B1-EC156','Course Name':'Sensor Tech',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Eswaran','Schedule':'YES','total_students':20},
    {'Department':'CSE','Semester':2,'Course Code':'B1-ASD152','Course Name':'Visual Design',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Sandesh','Schedule':'YES','total_students':15},
    # B2 basket (2 courses)
    {'Department':'CSE','Semester':2,'Course Code':'B2-DS151','Course Name':'Linux',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Layek','Schedule':'YES','total_students':25},
    {'Department':'CSE','Semester':2,'Course Code':'B2-CS151','Course Name':'Cybersecurity',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Rajendra','Schedule':'YES','total_students':20},
    # B4 basket (1 course)
    {'Department':'CSE','Semester':2,'Course Code':'B4-HS159','Course Name':'Quantum Physics',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Physics','Schedule':'YES','total_students':10},
]
pd.DataFrame(courses_11).to_csv('tests/TC-11/data/combined_even.csv', index=False)
write_rooms('tests/TC-11/data/rooms.csv', [
    ('R1','101',120,'LECTURE_ROOM'),('R2','102',120,'LECTURE_ROOM'),
    ('R3','103',60,'LECTURE_ROOM'),('R4','L101',60,'COMPUTER_LAB'),
    ('R5','L102',60,'COMPUTER_LAB'),
])
print('TC-11 fixed: 5 cores + B1(3) + B2(2) + B4(1)')

# --- FIX TC-14: 5 lab-only courses ---
courses_14 = []
profs = ['Dr. Alpha','Dr. Beta','Dr. Gamma','Dr. Delta','Dr. Epsilon']
for i, prof in enumerate(profs):
    courses_14.append({
        'Department':'CSE','Semester':2,'Course Code':f'CS1{60+i}',
        'Course Name':f'Lab Course {i+1}','L':0,'T':0,'P':2,'S':0,'C':2,
        'Faculty':prof,'Schedule':'YES','total_students':50,
        'Section':'ALL','SectionMode':'COMBINED'
    })
pd.DataFrame(courses_14).to_csv('tests/TC-14/data/combined_even.csv', index=False)
write_rooms('tests/TC-14/data/rooms.csv', [
    ('R1','L101',60,'COMPUTER_LAB'),('R2','L102',60,'COMPUTER_LAB'),
    ('R3','L103',60,'COMPUTER_LAB'),
])
print('TC-14 fixed: 5 lab-only courses, 3 labs')

# --- NEW TC-16: Schedule=NO Filter ---
os.makedirs('tests/TC-16/data', exist_ok=True)
courses_16 = [
    {'Department':'CSE','Semester':4,'Course Code':'CS401','Course Name':'Scheduled Course',
     'L':3,'T':1,'P':0,'S':0,'C':4,'Faculty':'Dr. A','Schedule':'YES','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':4,'Course Code':'CS402','Course Name':'Skipped Course 1',
     'L':3,'T':1,'P':0,'S':0,'C':4,'Faculty':'Dr. B','Schedule':'NO','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':4,'Course Code':'CS403','Course Name':'Skipped Course 2',
     'L':3,'T':0,'P':2,'S':0,'C':4,'Faculty':'Dr. C','Schedule':'NO','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
]
pd.DataFrame(courses_16).to_csv('tests/TC-16/data/combined_even.csv', index=False)
write_rooms('tests/TC-16/data/rooms.csv', [
    ('R1','101',100,'LECTURE_ROOM'),('R2','L101',60,'COMPUTER_LAB')
])
print('TC-16: Schedule=NO filtering')

# --- NEW TC-17: Empty Input ---
os.makedirs('tests/TC-17/data', exist_ok=True)
empty = pd.DataFrame(columns=['Department','Semester','Course Code','Course Name',
                               'L','T','P','S','C','Faculty','Schedule','total_students',
                               'Section','SectionMode'])
empty.to_csv('tests/TC-17/data/combined_even.csv', index=False)
write_rooms('tests/TC-17/data/rooms.csv', [('R1','101',100,'LECTURE_ROOM')])
print('TC-17: Empty input (0 courses)')

# --- NEW TC-18: Same Code Across 3 Depts (CE_SHARED) ---
os.makedirs('tests/TC-18/data', exist_ok=True)
courses_18 = [
    {'Department':'CSE','Semester':2,'Course Code':'MA163','Course Name':'Linear Algebra',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Anand','Schedule':'YES','total_students':110,
     'Section':'ALL','SectionMode':'COMBINED','CrossDeptGroup':'CE_SHARED_1','CrossDeptMode':'COMBINED'},
    {'Department':'DSAI','Semester':2,'Course Code':'MA163','Course Name':'Linear Algebra',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Anand','Schedule':'YES','total_students':132,
     'Section':'ALL','SectionMode':'COMBINED','CrossDeptGroup':'CE_SHARED_1','CrossDeptMode':'COMBINED'},
    {'Department':'ECE','Semester':2,'Course Code':'MA163','Course Name':'Linear Algebra',
     'L':3,'T':1,'P':0,'S':0,'C':2,'Faculty':'Dr. Anand','Schedule':'YES','total_students':83,
     'Section':'ALL','SectionMode':'COMBINED','CrossDeptGroup':'CE_SHARED_1','CrossDeptMode':'COMBINED'},
]
pd.DataFrame(courses_18).to_csv('tests/TC-18/data/combined_even.csv', index=False)
write_rooms('tests/TC-18/data/rooms.csv', [
    ('R1','C004',350,'LECTURE_ROOM'),('R2','102',100,'LECTURE_ROOM'),
])
print('TC-18: Same code, 3 depts, CE_SHARED')

# --- NEW TC-19: Room Reuse Across Semesters (1 room, 2 semesters) ---
os.makedirs('tests/TC-19/data', exist_ok=True)
courses_19 = [
    {'Department':'CSE','Semester':2,'Course Code':'CS201','Course Name':'Sem2 Course 1',
     'L':3,'T':1,'P':0,'S':0,'C':4,'Faculty':'Dr. A','Schedule':'YES','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':2,'Course Code':'CS202','Course Name':'Sem2 Course 2',
     'L':3,'T':0,'P':0,'S':0,'C':3,'Faculty':'Dr. B','Schedule':'YES','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':4,'Course Code':'CS401','Course Name':'Sem4 Course 1',
     'L':3,'T':1,'P':0,'S':0,'C':4,'Faculty':'Dr. C','Schedule':'YES','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':4,'Course Code':'CS402','Course Name':'Sem4 Course 2',
     'L':3,'T':0,'P':0,'S':0,'C':3,'Faculty':'Dr. D','Schedule':'YES','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
]
pd.DataFrame(courses_19).to_csv('tests/TC-19/data/combined_even.csv', index=False)
write_rooms('tests/TC-19/data/rooms.csv', [('R1','101',60,'LECTURE_ROOM')])
print('TC-19: 1 room, 2 semesters')

# --- NEW TC-20: 2-Hour Lecture Block ---
os.makedirs('tests/TC-20/data', exist_ok=True)
courses_20 = [
    {'Department':'CSE','Semester':4,'Course Code':'CS501','Course Name':'2hr Lecture Course',
     'L':2,'T':0,'P':0,'S':0,'C':2,'Faculty':'Dr. BlockTest','Schedule':'YES','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
    {'Department':'CSE','Semester':4,'Course Code':'CS502','Course Name':'Normal 3hr Lecture',
     'L':3,'T':1,'P':0,'S':0,'C':4,'Faculty':'Dr. NormalTest','Schedule':'YES','total_students':50,
     'Section':'ALL','SectionMode':'COMBINED'},
]
pd.DataFrame(courses_20).to_csv('tests/TC-20/data/combined_even.csv', index=False)
write_rooms('tests/TC-20/data/rooms.csv', [
    ('R1','101',100,'LECTURE_ROOM'),('R2','102',100,'LECTURE_ROOM')
])
print('TC-20: 2-hour lecture block')

print('\n=== ALL DATA FILES GENERATED ===')
