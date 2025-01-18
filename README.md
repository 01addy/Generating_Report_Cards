# Generating_Report_Cards
Generating Report Cards from Excel (PDF form)
You are given an Excel file named student_scores.xlsx containing the following columns:

Student ID | Name | Math Score | Science Score

A Python script that does the following:
Reads the data from the Excel file using the pandas library. Groups the data by student and calculates their total and average scores across all subjects. Generates a personalized PDF report card for each student using the ReportLab library. Each report card should include: Student Name / Total Score / Average Score/ A table showing subject-wise scores. Save the PDF files with the naming format report_card_<StudentID>.pdf. Ensure that your script includes proper error handling for missing or invalid data in the Excel file.
