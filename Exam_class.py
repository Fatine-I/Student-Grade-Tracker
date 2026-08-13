class Exam(Assignment):
    def __init__(self,subject,title,score,max_score,due_date):
        super().__init__(subject,title,score,max_score,due_date,"exam")
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