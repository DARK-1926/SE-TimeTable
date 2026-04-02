import pandas as pd
import os

input_path = r"c:\Users\mohit\Downloads\combined1 - Sheet1.csv"
output_path = r"c:\Users\mohit\Downloads\SE TT\Automated-Time-Table-Scheduling-at-IIIT-Dharwad\data\combined_even.csv"

# Read the CSV
# Using sep=None, engine='python' to auto-detect and handle issues
df = pd.read_csv(input_path)

# 1. Strip all string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# 2. Fix the split line bug in faculty name (B5-CS373)
# If the line was read correctly by pandas (due to quotes), the newline is in the string.
df['Faculty'] = df['Faculty'].str.replace('\n', ' ').str.replace('\r', ' ')

# 3. Remove the extra empty column (if any)
df = df.iloc[:, :16] # Keep only the first 16 columns

# 4. Filter out any totally empty rows
df = df.dropna(how='all')

# 5. Fix L, T, P, S, C columns (ensure they are integers where possible)
for col in ['L', 'T', 'P', 'S', 'C', 'Semester', 'total_students']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# 6. Save to output
df.to_csv(output_path, index=False)
print(f"✅ Cleaned and saved to {output_path}")
