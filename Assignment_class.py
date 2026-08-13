class Assignment(Course):
    def __init__(self, subject,title,assignment_type,score,max_score,due_date):#.....constructor method for class Assignment objects
        self.subject=subject
        self.title=title
        self.score=score
        self.max_score=max_score
        self.due_date=datetime.datetime.strptime('%Y-%m-%d %H:%M:%S').date()