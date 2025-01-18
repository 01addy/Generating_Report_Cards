import pandas as pd

# Create sample data for 10 students
data = {
    "Student ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": [
        "John Doe", "Jane Smith", "Alice Brown", "Bob Johnson", "Charlie Lee",
        "Daisy Clark", "Eve Adams", "Frank Miller", "Grace Hill", "Henry Wilson"
    ],
    "Math Score": [95, 85, 78, 92, 76, 89, 91, 88, 90, 94],
    "Science Score": [90, 88, 82, 87, 80, 84, 85, 86, 88, 89]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Save to an Excel file
file_path = r"C:\Users\8858s\OneDrive\Desktop\Python Intern\student_scores.xlsx"  # Use raw string to avoid path issues
df.to_excel(file_path, index=False)

print(f"Excel file generated at: {file_path}")
