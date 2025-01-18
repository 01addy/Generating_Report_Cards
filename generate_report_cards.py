import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
import os

# Function to generate a report card PDF for each student
def generate_report_card(student_id, name, math_score, science_score):
    # Ensure the output directory exists
    output_dir = 'output_reports'
    os.makedirs(output_dir, exist_ok=True)  # Creates the directory if it doesn't exist

    # Define the filename for the PDF
    pdf_filename = os.path.join(output_dir, f'report_card_{student_id}.pdf')
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)  # Setting up the PDF document
    styles = getSampleStyleSheet()  # Using ReportLab's default styles
    elements = []  # List to hold content for the PDF

    # Add title to the report card
    title = Paragraph(f"Report Card for {name} (ID: {student_id})", styles['Title'])
    elements.append(title)

    # Calculate total and average scores
    total_score = math_score + science_score
    average_score = total_score / 2

    # Add total and average scores
    elements.append(Paragraph(f"Total Score: {total_score}", styles['Normal']))
    elements.append(Paragraph(f"Average Score: {average_score:.2f}", styles['Normal']))

    # Add a table for subject-wise scores
    data = [["Subject", "Score"], ["Math", math_score], ["Science", science_score]]
    table = Table(data)
    elements.append(table)

    # Build the PDF
    document.build(elements)
    print(f"Report card generated: {pdf_filename}")


# Main function
def main():
    try:
        # Read the Excel file
        df = pd.read_excel(r'C:\Users\8858s\OneDrive\Desktop\Python Intern\student_scores.xlsx')  # Replace with the correct path to your Excel file

        # Check for required columns
        required_columns = {'Student ID', 'Name', 'Math Score', 'Science Score'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Excel file must contain the following columns: {', '.join(required_columns)}")

        # Generate report cards for each student
        for _, row in df.iterrows():
            student_id = row['Student ID']
            name = row['Name']
            math_score = row['Math Score']
            science_score = row['Science Score']
            generate_report_card(student_id, name, math_score, science_score)

    except FileNotFoundError:
        print("Error: The file 'student_scores.xlsx' was not found.")  # Handle missing file error
    except ValueError as ve:
        print(f"Value Error: {ve}")  # Handle validation errors
    except Exception as e:
        print(f"An error occurred: {e}")  # Catch all other exceptions


# Entry point of the script
if __name__ == '__main__':
    main()
