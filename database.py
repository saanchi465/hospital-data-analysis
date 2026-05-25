import sqlite3
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\navee\Desktop\saanchi\Intern\hospital data analysis.csv")

# Show columns
print(df.columns)

# Create database
conn = sqlite3.connect("healthcare.db")

# Store dataset into SQL table
df.to_sql(
    'patients',
    conn,
    if_exists='replace',
    index=False
)

print("\nDatabase Created Successfully!")

# SQL Query
query = """
SELECT Condition, COUNT(*) as Total_Patients
FROM patients
GROUP BY Condition
ORDER BY Total_Patients DESC
"""

# Execute query
result = pd.read_sql(query, conn)

print("\nCondition Analysis:\n")

print(result)

conn.close()