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