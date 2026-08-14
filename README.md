# Student-Grade-Tracker
Programming 1 - Formative project; allows users to record homework and exam results, view and filter assignments, and display grade summaries within a single terminal session. 

PROJECT OVERVIEW & FEATURES:

PROJECT OVERVIEW:
Grade Tracker is a session-only Python application for recording homework and exam results. 
It demonstrates strings, conditionals, loops, functions, collections, classes, inheritance, and input validation. 
The program stores assignments in memory and provides listing, filtering, and summary features.

FEATURES:
- Add homework or exams with subject, title, score, maximum score, and due date.
- List all assignments in a readable format.
- Filter by subject, assignment type, or month (YYYY-MM).
- View overall and per-subject averages plus the highest and lowest assignments.
- Rejects invalid menu choices, blank text, invalid numbers, impossible scores, and invaliddates.
- Does not save files; all data is cleared when the program exits.

REPOSITORY STRUCTURE:
This repository uses separate branches to allow independent development of each class:
-> main — default branch with the complete program.
-> Assignment — the Assignment class.
-> Course — the Course class.
-> Exam— the Exam class.
-> Homework — the Homework class.
-> Grade_Tracker — changes to the GradeTracker class.

The main branch contains:
-> main.py — menu and program entry point.
-> GradeTracker_full_code.py — combined code with all classes and the main function.

Other branches contain only the relevant class file so that changes can be done and tested in isolation before merging.


INSTRUCTIONS TO RUN THE PROGRAM:
1. Install Python 3.
2. Clone the repository to your computer.
3. Open a terminal in the repository folder.
4. Run the following commands: python GradeTracker_full_code.py


MENU SRUCTURE:

GRADE TRACKER
  1. Add homework
  2. Add exam
  3. List assignments
  4. Filter assignments
  5. Show summary
  6. Exit



SAMPLE INTERACTIONS:

Adding homework:
'''
Choose an option: 1
Enter valid subject: Math
Enter valid title: Algebra
Score: 18
Maximum score: 20
Due date (YYY-MM-DD): 2025-10-15
Homework added successfully!
'''

Adding exam:
'''
Choose an option: 2
Enter valid subject: Physics
Enter valid title: Mechanics
Score: 42
Maximum score: 50
Due date (YYY-MM-DD): 2025-10-22
Exam added successfully!
'''

Listing Assignments:
'''
Choose an option: 3
Assignment 1 (Homework):
Subject: Math | Title: Algebra | Score: 18.0 / 20.0 | Due date: 2025-10-15
Assignment 2 (Exam):
Subject: Physics | Title: Mechanics | Score: 42.0 / 50.0 | Due date: 2025-10-22
'''

Filtering Assignments:
'''
Choose an option: 4
Enter subject, type, or month (YYYY-MM): 2025-10
Assignments matching '2025-10':
Assignment 1 (Homework):
Subject: Math | Title: Algebra | Score: 18.0 / 20.0 | Due date: 2025-10-15
Assignment 2 (Exam):
Subject: Physics | Title: Mechanics | Score: 42.0 / 50.0 | Due date: 2025-10-22

Showing the Summary:
'''
Choose an option: 5
GRADE SUMMARY
Overall average: 86.67%
Per-subject averages:
Math: 90.00%
Physics: 84.00%
Highest scoring assignment:
Algebra | Math) | 90.00%
Lowest scoring assignment:
Mechanics | Physics) | 84.00%
'''
