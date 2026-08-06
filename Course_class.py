class Course:
    def __init__(self,course):
        self.course=course.dict()
        self.subject=course.key()
        self.title=course.value()
        course={
            'Math':('Algebra','Geometry','Trigonometry'),
            'Physics':('Thermodynamics', 'Mechanics', 'Electromagnetism'),
            'Computer_Science':('Computer Architecture','Software Applications','Programming')
        }