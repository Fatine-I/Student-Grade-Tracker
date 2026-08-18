
import time
from datetime import datetime


class Course:
    def __init__(self):
        self.course={
            'Math':('Algebra','Geometry','Trigonometry'),
            'Physics':('Thermodynamics', 'Mechanics', 'Electromagnetism'),
            'Computer_Science':('Computer Architecture','Software Applications','Programming')
        }





class Assignment(Course):
    def __init__(self, subject,title,score,max_score,due_date,assignment_type):#.....constructor method for class Assignment objects
        self.subject=subject
        self.title=title
        self.score=score
        self.max_score=max_score
        self.due_date=due_date
        self.assignment_type=assignment_type





class Exam(Assignment):
    def __init__(self,subject,title,score,max_score,due_date):
        super().__init__(subject,title,score,max_score,due_date,"Exam")
        self.exam_list = []

    def add_exam(self, subject, title, due_date, max_score, graded=False, score=None):
        self.exam_list.append({
            "subject": subject,
            "title": title,
            "due_date": due_date,
            "max_score": max_score,
            "grade": graded,
            "scores": [] if score is None else [score]
        })





class Homework(Assignment):
    def __init__(self,subject,title,score,max_score,due_date):
        super().__init__(subject,title,score,max_score,due_date,"Homework")
        self.homework_list = []

    def add_homework(self, subject, title, due_date, max_score, graded=False,score=None):
        self.homework_list.append({
            "subject": subject,
            "title": title,
            "due_date": due_date,
            "max_score": max_score,
            "graded": graded,
            "scores": [] if score is None else [score]
        })





class GradeTracker(Course):
    def __init__(self):
        super().__init__()
        self.assignments=[]
    def total_score(self,scores):
        if not scores:
            return 0
        return sum(scores)

    def average_scores(self, scores):
        if not scores:
            return 0
        return self.total_score(scores)/len(scores)

    def percentage_score(self,score,max_score):
        if max_score == 0:
            return 0
        return (score/max_score)*100

    def get_subject(self):
        while True:
            subject=input("Enter valid subject:").strip()
            if subject in self.course.keys():
                return subject
            else:
                print("Subject not available.")
                print("\nAvailable subject are:")
                for subject_name in self.course.keys():
                    print(f"- {subject_name}")

    def get_title(self, subject):
        while True:
            title=input("Enter valid title: ").strip()
            if title in self.course[subject]:
                return title
            else:
                print("Title not available for this subject.")
                print(f"\nAvailable titles for {subject}:")
                for title in self.course[subject]:
                    print(f"-{title}")

    def get_score(self):
        while True:
            try:
                score = float(input("Score: "))
                if score < 0:
                    raise ValueError("Score cannot be negative.")
                return score
            except ValueError as e:
                print(f"Invalid score: {e}")

    def get_max_score(self):
        while True:
            try:
                max_score = float(input("Maximum score: "))
                if max_score <= 0:
                    raise ValueError("Maximum score must be greater than 0.")
                return max_score
            except ValueError as e:
                print(f"Invalid maximum score: {e}")

    def get_due_date(self):
        while True:
            due_date=input("Due date (YYY-MM-DD): ").strip()
            try:
                return datetime.strptime(due_date,"%Y-%m-%d").date()
            except ValueError:
                print("Invalid date.\nUse YYYY-MM-DD format")



    def add_homework(self):
        subject=self.get_subject()
        title=self.get_title(subject)
        score=self.get_score()
        max_score=self.get_max_score()
        while score>max_score:
            print("Score cannot be greater than\nthe maximum score.")
            score=self.get_score()
        due_date=self.get_due_date()
        homework = Homework(subject,title,score,max_score,due_date)
        self.assignments.append(homework)
        print("\nHomework added successfully!")

    def add_exam(self):
        subject=self.get_subject()
        title=self.get_title(subject)
        score=self.get_score()
        max_score=self.get_max_score()
        while score>max_score:
            print("Score cannot be greater than\nthe maximum score.")
            score=self.get_score() 
        due_date=self.get_due_date()
        exam = Exam(subject,title,score,max_score,due_date)
        self.assignments.append(exam)
        print("\nExam added successfully!")



    def overall_percentage(self):
        if not self.assignments:
            return None
        total_score=self.total_score([assignment.score for assignment in self.assignments])
        total_max=self.total_score([assignment.max_score for assignment in self.assignments])
        return self.percentage_score(total_score,total_max)

    def subject_percentage(self, subject):
        subject_assignments = [assignment for assignment in self.assignments if assignment.subject == subject]
        if not subject_assignments:
            return None
        total_score = self.total_score([assignment.score for assignment in subject_assignments])
        total_max = self.total_score([assignment.max_score for assignment in subject_assignments])
        return self.percentage_score(total_score,total_max)

    def highest_lowest_assignment(self):
        if not self.assignments:
            return None, None
        highest = max(self.assignments,key=lambda assignment:self.percentage_score(assignment.score,assignment.max_score))
        lowest = min(self.assignments,key=lambda assignment:self.percentage_score(assignment.score,assignment.max_score))
        return highest, lowest

    def list_assignments(self):
        if not self.assignments:
            print("No assignments recorded.")
            return
        for number, assignment in enumerate(self.assignments,start=1):    
            print(f"\nAssignment {number} ({assignment.assignment_type.title()}):\n")
            print(f"Subject:{assignment.subject} | Title: {assignment.title} | Score: {assignment.score} / {assignment.max_score} | Due date: {assignment.due_date}")



    def filter_assignments(self):
        if not self.assignments:
            print("\nThere are no assignments to filter.")
            return
        keyword=input("Enter subject, type, or month (YYYY-MM):").strip().lower()
        found=[]
        for assignment in self.assignments:
            subject=assignment.subject.lower()
            assignment_type=assignment.assignment_type.lower()
            month=assignment.due_date.strftime("%Y-%m")
            if(keyword in subject or keyword == assignment_type or keyword == month):
                found.append(assignment)
        if not found:
            print(f"\nNo assignments found matching '{keyword}'.")
            return
        print(f"\nAssignments matching '{keyword}':")
        for number, assignment in enumerate(found, start=1):
            print(f"\nAssignment {number} ({assignment.assignment_type.title()}):\n")
            print(f"Subject:{assignment.subject} | Title: {assignment.title} | Score: {assignment.score} / {assignment.max_score} | Due date: {assignment.due_date}")



    def summary(self):
        print("GRADE SUMMARY\n\n")   
        if not self.assignments:
            print("\nNo assignments recorded.")
            return

        overall = self.overall_percentage()
        print(f"\nOverall average: {overall:.2f}%")
        print("\nPer-subject averages:\n")
        subjects = []
        for assignment in self.assignments:
            subjects.append(assignment.subject)
        for subject in subjects:
            percentage = self.subject_percentage(subject)
            print(f"{subject}: {percentage:.2f}%")

        highest, lowest = (self.highest_lowest_assignment())
        highest_percentage = self.percentage_score(highest.score,highest.max_score)
        lowest_percentage = self.percentage_score(lowest.score,lowest.max_score)
        print("\nHighest scoring assignment:\n")
        print(f"{highest.title} | {highest.subject}) | {highest_percentage:.2f}%")
        print("\nLowest scoring assignment:\n")
        print(f"{lowest.title} | {lowest.subject}) | {lowest_percentage:.2f}%")

    def undo_last_entry(self):
        if not self.assignments:
                    print("No assignments recorded.")
                    return
        for number, assignment in enumerate(self.assignments,start=1):
            self.assignments.pop()
        print("last item removed successfully!") 
        







def main():
    tracker=GradeTracker()
    while True:
        print("GRADE TRACKER\n\n\n")
        print("1. Add homework")
        print("2. Add exam")
        print("3. List assignments")
        print("4.Filter assignments")
        print("5. Show summary")
        print("6. Undo last entry")
        print("7. Exit")
        choice=input("\nChoose an option: ").strip()
        if choice=="1":
            tracker.add_homework() 
            input("\nPress Enter to return to the main menu")
        elif choice == "2":
            tracker.add_exam()
            input("\nPress Enter to return to the main menu")
        elif choice=="3":
            tracker.list_assignments()
            input("\nPress Enter to return to the main menu")
        elif choice=="4":
            tracker.filter_assignments()
            input("\nPress Enter to return to the main menu")
        elif choice=="5":
            tracker.summary()
            input("\nPress Enter to return to the main menu")
        elif choice=="6":
            tracker.undo_last_entry()
            input("\nPress Enter to return to the main menu")
        elif choice=="7":
            break
        else:
            print("\nInvalid choice. Please choose 1-6")
            input("\nPress Enter to return to the main menu")

if __name__=="__main__":
    print("Initial setup test: program started successfully.") 
    main()

    