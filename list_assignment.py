import time
import datetime

assignment_types=("homework","exam")
class Assignment(Course):
    def __init__(self, subject,title,assignment_type,score,max_score,due_date):#.....constructor method for class Assignment objects
        self.subject=subject
        self.title=title
        self.assignment_type=assignment_type
        self.score=score
        self.max_score=max_score
        self.due_date=datetime.datetime.strptime('%Y-%m-%d %H:%M:%S').date()
        self.today=datetime.datetime.today()
        self.homework=Homework()
        self.exam=Exam()
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
                    self.homework.add_homework(
                        self.subject,
                        self.title,
                        self.due_date
                    )
                elif self.assignment_type == "exam":
                    self.exam.add_exam(
                        self.subject,
                        self.title,
                        self.due_date
                    )
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

        print("   PENDING ASSIGNMENTS    ")
        print("________________________\n")

        if self.homework.homework_list:
            print("HOMEWORK\n")
            print("________")

        for number, homework in enumerate(
                self.homework.homework_list, start=1):

            print(f"Homework {number}")
            print(f"Subject:  {homework['subject']}")
            print(f"Title:    {homework['title']}")
            print(f"Due date: {homework['due_date']}")
            print()

        else:
            print("No homework assignments.\n")


        if self.exam.exam_list:
            print("EXAMS")
            print("_____")

        for number, exam in enumerate(
                self.exam.exam_list, start=1):

            print(f"Exam {number}")
            print(f"Subject:  {exam['subject']}")
            print(f"Title:    {exam['title']}")
            print(f"Due date: {exam['due_date']}")
            print()

        else:
            print("No exams.\n")


    def display_assignment(self, assignment, assignment_type):
        print(f"\n{assignment_type}")
        print(f"Subject:  {assignment['subject']}")
        print(f"Title:    {assignment['title']}")
        print(f"Due date: {assignment['due_date']}")


    def filter_assignment(self):
        if not self.homework.homework_list and not self.exam.exam_list:
            print("\nThere are no assignments to filter.")
            return

        keyword = input("\nEnter subject, assignment type, or month to filter: ").strip().lower()

        found = False
        print("FILTERED ASSIGNMENTS")
        print("____________________")

        for homework in self.homework.homework_list:
            due_date = homework["due_date"]

            if (
            keyword in homework["subject"].lower()#..................................using a keyword in subject
            or keyword in "homework"#................................................using a keyword in the assignment_type ('homework')
            or keyword in due_date.strftime("%B").lower()#...........................using a keyword in the month name
            or keyword in due_date.strftime("%b").lower()#...........................using a keyword in the short-term name of the month (ex. Aug instead of August)
            or keyword == due_date.strftime("%m")#...................................using a keyword in the month number
            ):
                self.display_assignment(homework, "Homework")
                found = True

        for exam in self.exam.exam_list:
            due_date = exam["due_date"]

            if (
            keyword in exam["subject"].lower()
            or keyword in "exam"
            or keyword in due_date.strftime("%B").lower()
            or keyword in due_date.strftime("%b").lower()
            or keyword == due_date.strftime("%m")
            ):
                self.display_assignment(exam, "Exam")
                found = True

        if not found:
            print("\nNo assignments found matching:", keyword)
            

        

class Course:#.......................................................................class for courses having the subjects and titles
    def __init__(self):
        self.course={
            'Math':('Algebra','Geometry','Trigonometry'),
            'Physics':('Thermodynamics', 'Mechanics', 'Electromagnetism'),
            'Computer_Science':('Computer Architecture','Software Applications','Programming')
        }

class Homework:
    def __init__(self):
        self.homework_list = []

    def add_homework(self, subject, title, due_date):
        self.homework_list.append({
            "subject": subject,
            "title": title,
            "due_date": due_date
        })

class Exam:
    def __init__(self):
        self.exam_list = []

    def add_exam(self, subject, title, due_date):
        self.exam_list.append({
            "subject": subject,
            "title": title,
            "due_date": due_date
        })

