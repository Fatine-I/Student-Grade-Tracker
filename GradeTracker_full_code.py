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