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