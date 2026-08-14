import time
import datetime

assignment_types=("homework","exam")
class Assignment(Course,Grade_Tracker):
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
        Course.__init__(self)



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
    

    scores=homework["scores"]
    average=self.average_score(scores)
    print(average)

    percentage = self.percentage_score(average,homework["max_score"])



    def all_assignments(self): 
        assignments=[]
        for homework in self.homework.homework_list:
           assignments.append({**homework, "type": "homework"})
        for exam in self.exam.exam_list:
            assignments.append({**exam,"type": "exam"})



    def subject_grade(self,assignment_list,subject):
        assignment_list=self.all_assignments()
        subject_scores=[]
        subject_max_scores=[]
        for assignment in assignment_list:
            if assignment["subject"]== subject:
                if assignment["scores"]:
                    average=self.average_score(assignment["scores"])
                    subject_scores.append(average)
                    subject_max_scores.append(assignment["max_score"])
        total=self.total_score(subject_scores)
        max_total=self.total_score(subject_max_scores)
        percentage=self.percentage_score(total,max_total)
        return total, max_total, percentage


    def assignment_type_grade(self, assignment_list):
        scores = []
        max_scores=[]
        for assignment in assignment_list:
            if assignment["scores"]:
                average=self.average_score(assignment["scores"])
        total=self.total_score(scores)
        max_total=self.total_score(max_scores)
        percentage=self.percentage_score(total,max_total)   
        return total,max_total, percentage



    homework_total, homework_max, homework_percentage = self.assignment_type_grade(self.homework.homework_list)


    exam_total, exam_max, exam_percentage=self.assignment_type_grade(self.exam.exam_list)



    def course_grade(self):
        homework_total,homework_max, _ = self.assignment_type_grade(sefl.homework.homework_list)
        exam_total,exam_max, _ = self.assignment_type_grade(self.exam.exam_list)
        total=self.total_score([homework_total,exam_total])
        max_total=self.total_score([homework_max,exam_max])
        percentage=self.percentage_score(total,max_total)
        return total, max_total, percentage



    def highest_lowest_assignment(self):

        assignments = self.all_assignments()

        graded_assignments = []

        for assignment in assignments:

            if (assignment["graded"] and assignment["scores"]):
                average = self.average_score(assignment["scores"])
                percentage = self.percentage_score(average,assignment["max_score"])

            graded_assignments.append({
                "assignment": assignment,
                "average": average,
                "percentage": percentage
            })

    if not graded_assignments:
        print("\nThere are no graded assignments.")
        return

    highest = max(
        graded_assignments,
        key=lambda x: x["percentage"]
    )

    lowest = min(
        graded_assignments,
        key=lambda x: x["percentage"]
    )

    print("\n==============================")
    print(" HIGHEST SCORING ASSIGNMENT")
    print("==============================")

    assignment = highest["assignment"]

    print(f"Type:       {assignment['type'].title()}")
    print(f"Subject:    {assignment['subject']}")
    print(f"Title:      {assignment['title']}")
    print(f"Average:    {highest['average']:.2f}")
    print(f"Percentage: {highest['percentage']:.2f}%")

    print(" LOWEST SCORING ASSIGNMENT")
    print("__________________________")

    assignment = lowest["assignment"]

    print(f"Type:       {assignment['type'].title()}")
    print(f"Subject:    {assignment['subject']}")
    print(f"Title:      {assignment['title']}")
    print(f"Average:    {lowest['average']:.2f}")
    print(f"Percentage: {lowest['percentage']:.2f}%")



def top_performing_subjects(self):

    assignments = self.all_assignments()

    subjects = set()

    for assignment in assignments:

        if assignment["graded"]:
            subjects.add(
                assignment["subject"]
            )

    subject_grades = []

    for subject in subjects:

        percentage = self.subject_grade(
            subject
        )

        if percentage is not None:

            subject_grades.append(
                (subject, percentage)
            )

    if not subject_grades:

        print("\nThere are no graded subjects.")
        return

    subject_grades.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n==============================")
    print(" TOP PERFORMING SUBJECTS")
    print("==============================")

    for number, (subject, percentage) in enumerate(
        subject_grades,
        start=1
    ):

        print(
            f"{number}. {subject}: "
            f"{percentage:.2f}%"
        )



def low_score_warnings(self):

    assignments = self.all_assignments()

    valid = False

    while not valid:

        try:

            threshold = float(
                input(
                    "\nEnter grade threshold (%): "
                )
            )

            if threshold < 0 or threshold > 100:

                raise ValueError(
                    "Threshold must be between 0 and 100."
                )

            valid = True

        except ValueError as e:
            print(e)

    warnings = []

    for assignment in assignments:

        if (
            assignment["graded"]
            and assignment["scores"]
        ):

            average = self.average_score(
                assignment["scores"]
            )

            percentage = self.percentage_score(
                average,
                assignment["max_score"]
            )

            if percentage < threshold:

                warnings.append({
                    "assignment": assignment,
                    "average": average,
                    "percentage": percentage
                })

    print("\n==============================")
    print("       LOW-SCORE WARNINGS")
    print("==============================")

    if not warnings:

        print(
            f"\nNo assignments are below "
            f"{threshold:.2f}%."
        )

        return

    for warning in warnings:

        assignment = warning["assignment"]

        print(
            f"\n{assignment['type'].title()}"
        )

        print(
            f"Subject:    {assignment['subject']}"
        )

        print(
            f"Title:      {assignment['title']}"
        )

        print(
            f"Percentage: "
            f"{warning['percentage']:.2f}%"
        )



     def summary(self):

    print("\n================================")
    print("        GRADE SUMMARY")
    print("================================")

    # --------------------------------------------------------
    # OVERALL GRADE
    # --------------------------------------------------------

    overall = self.overall_grade()

    if overall is None:

        print(
            "\nOverall grade: No graded assignments."
        )

    else:

        print(
            f"\nOverall percentage grade: "
            f"{overall:.2f}%"
        )


    # --------------------------------------------------------
    # SUBJECT GRADES
    # --------------------------------------------------------

    assignments = self.all_assignments()

    subjects = set()

    for assignment in assignments:

        if assignment["graded"]:
            subjects.add(
                assignment["subject"]
            )

    print("\nPer-subject percentage grades:")
    print("--------------------------------")

    if not subjects:

        print("No graded subjects.")

    else:

        for subject in sorted(subjects):

            percentage = self.subject_grade(
                subject
            )

            if percentage is not None:

                print(
                    f"{subject}: "
                    f"{percentage:.2f}%"
                )


    # --------------------------------------------------------
    # MORE OPTIONS
    # --------------------------------------------------------

    print("\n================================")
    print("          MORE OPTIONS")
    print("================================")

    print("1. Highest/lowest scoring assignment")
    print("2. Top performing subjects")
    print("3. Grade threshold / low-score warnings")
    print("4. Return")

    valid = False

    while not valid:

        try:

            option = input(
                "\nChoose an option: "
            ).strip()

            if option not in (
                "1",
                "2",
                "3",
                "4"
            ):

                raise ValueError(
                    "Please choose an option from 1 to 4."
                )

            valid = True

        except ValueError as e:
            print(e)


    if option == "1":

        self.highest_lowest_assignment()

    elif option == "2":

        self.top_performing_subjects()

    elif option == "3":

        self.low_score_warnings()

    elif option == "4":

        return



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



    def all_assignments(self):
        assignments = []
        for homework in self.homework.homework_list:
            assignments.append({**homework,"type": "homework"})
        for exam in self.exam.exam_list:
            assignments.append({**exam,"type": "exam"})
        return assignments

        

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

    def add_homework(self, subject, title, due_date, max_score, graded=False,score=None):
        self.homework_list.append({
            "subject": subject,
            "title": title,
            "due_date": due_date,
            "max_score": max_score,
            "graded": graded,
            "scores": [] if score is None else [score]
        })

class Exam:
    def __init__(self):
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

class Grade_Tracker:
    def __init__(self):
        pass
    def total_score(self, scores):
        if not scores:
            return 0
        return sum(scores)

    def average_score(self, scores):
        if not scores:
            return None
        return self.total_score(scores)/len(score)

    def percentage_score(self,score,max_score):
        if max_score == 0:
            return None
        return (score/ max_score)*100







def main():

    assignment = Assignment()

    while True:

        print("\n================================")
        print("       GRADE TRACKER")
        print("================================")

        print("1. Add assignment")
        print("2. List assignments")
        print("3. Filter assignments")
        print("4. Show summary")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        # --------------------------------------------
        # 1. ADD ASSIGNMENT
        # --------------------------------------------

        if choice == "1":

            while True:

                assignment.add_assignment()

                print("\n--------------------------------")
                print("1. Add another assignment")
                print("2. Return to main menu")
                print("--------------------------------")

                option = input(
                    "Choose an option: "
                ).strip()


    def return_to_menu(self):

    input(
        "\nPress Enter to return to "
        "the main menu..."
    )
    
    elif choice == "2":

    assignment.list_assignment()
    assignment.return_to_menu()

elif choice == "3":

    assignment.filter_assignment()
    assignment.return_to_menu()

elif choice == "4":

    assignment.summary()
    assignment.return_to_menu()