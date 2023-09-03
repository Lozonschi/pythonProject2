class Education:
    def __init__(self, degree, school, year, additional_info=None):
        self.degree = degree
        self.school = school
        self.year = year
        self.additional_info = additional_info if additional_info is not None else []