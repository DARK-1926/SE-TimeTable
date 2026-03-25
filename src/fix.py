import re

path = r"c:\Users\mohit\Downloads\SE TT\Automated-Time-Table-Scheduling-at-IIIT-Dharwad\src\Class_TT.py"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for candidate_room or room
pattern = r"([ \t]+)if (candidate_room|room) not in room_schedule:\n\1    room_schedule\[\2\] = \{d: set\(\) for d in range\(len\(DAYS\)\)\}\n\1room_schedule\[\2\]\[day\]\.add\(si\)"

def repl(m):
    indent = m.group(1)
    var = m.group(2)
    return f"{indent}for crn in str({var}).split('+'):\n{indent}    if crn not in room_schedule:\n{indent}        room_schedule[crn] = {{d: set() for d in range(len(DAYS))}}\n{indent}    room_schedule[crn][day].add(si)"

new_content, count = re.subn(pattern, repl, content)
print(f"Replaced {count} occurrences")

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
