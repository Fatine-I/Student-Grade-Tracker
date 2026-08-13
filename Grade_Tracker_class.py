import time
import datetime



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

    def add_homework(self):
        pass

    def add_exam(self):
        pass
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

    def get_score(self, score):
        while True:
            try:
                score = float(score)
                if score < 0:
                    raise ValueError("Score cannot be negative.")
                return score
            except ValueError as e:
                print(f"Invalid score: {e}")

    def get_max_score(self,max_score):
        while True:
            try:
                max_score = float(max_score)
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
            

    