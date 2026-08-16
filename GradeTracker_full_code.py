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