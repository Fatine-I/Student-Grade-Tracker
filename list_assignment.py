import time
import datetime

class Assignment(Course):
    def __init__(self, subject,title,assignment_type,score,max_score,due_date):#.....constructor method for class Assignment objects
        self.subject=subject
        self.title=title
        self.assignment_type=("homework","exam")
        self.score=score
        self.max_score=max_score
        self.due_date=datetime.datetime.strptime('%Y-%m-%d %H:%M:%S').date()
        self.today=datetime.datetime.today()
        super().__init__()



    def add_assignment(self):#.......................................................recording a new assignment in existing course, subject and title

        while self.subject not in self.course.keys():
            try:
                subject=input("Enter valid subject: ")
                if self.subject not in self.course.keys():
                    raise ValueError("Subject not available.")
            except ValueError as e:
                print(e)

        while self.title not in self.course[self.subject]:
            try:
                self.title=input("Enter valid title: ")
                if self.title not in self.course[self.subject]:
                    raise ValueError("Title not available for this subject.")
            except ValueError as e:
                print(e)

        while self.assignment_type not in Assignment.assignment_type:
            try:
                self.assignment_type=input("Enter valid Assignment type:")
                if self.assignment_type not in Assignment.assignment_type:
                    raise ValueError("Invalid assignment type.")
                if self.assignment_type == "homework":
                    homework_list=Homework(self.subject,self.title,self.due_date)
                elif self.assignment_type == "exam":
                                    exam_list=Exam(self.subject,self.title,self.due_date)
            except ValueError as e:
                print(e)

        while self.score>self.max_score:
            try:
                self.score=float(input('Score: '))
                self.max_score=float(input("Maximum Score: "))
                if self.score>self.max_score:
                    raise ValueError("Score cannot exceed maximum score.")
            except (ValueError,TypeError,NameError) as e:
                print(e)

        print("\nAssignment recorded successfully")


    def find_date_difference(self):
        date_difference=self.due_date - self.today
        if date_difference.total_seconds()>0:
            days=date_difference.days
            hours, remainder=divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"{abs(days)} remaining until the deadline.\n")
            print(f"Time left: {days}days {hours}:{minutes}:{seconds}", end="\r")
            time.sleep(1)
            
        elif date_difference.days<0:
            return f"{abs(days)} days past the deadline.\n"
        else:
            return f"The deadline is today"
    

    def list_assignment(self):
        print("Pending assignments:\n")
        print("Graded assignments:\n")

            

        

class Course:#.......................................................................class for courses having the subjects and titles
    def __init__(self):
        self.course={
            'Math':('Algebra','Geometry','Trigonometry'),
            'Physics':('Thermodynamics', 'Mechanics', 'Electromagnetism'),
            'Computer_Science':('Computer Architecture','Software Applications','Programming')
        }

class Homework():
    def __init__(self,subject,title,due_date):
        self.homework_list=[]
        self.subject=subject
        self.title=title
        self.due_date=datetime.datetime.strptime('%Y-%m-%d %H:%M:%S').date()
        self.homework_list.append({"subject": subject, "title": title, "due_date": due_date})

class Exam:
    def __init__(self,subject,title,due_date):
        self.exam_list=[]
        self.subject=subject
        self.title=title
        self.due_date=datetime.datetime.strptime('%Y-%m-%d %H:%M:%S').date()
        self.exam_list.append({"subject": subject, "title": title, "due_date": due_date})

