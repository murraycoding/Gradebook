class Category:

    def __init__(self, name, course, average, points, weight, graded):
        self.name = name
        self.course = course
        self.average = average
        self.points = points
        self.weight = weight
        self.graded = graded      # a boolean value to determine if the assignment is an average of other categories or just a graded assignment

# A course will be made up of several units
class Unit(Category):

    def __init__(self, name, course, average, points, weight, graded, number, standards = []):
        super().__init__(name, course, average, points, weight, graded)
        self.number = number            # integer
        self.standards = standards      # object []

    def __repr__(self):
        return f'{self.course} - Unit {self.number}: {self.name}'

# A unit will be made up of several standards
class Standard(Category):

    def __init__(self, name, course, average, points, weight, graded, unit, number, assignments = []):
        super().__init__(name, course, average, points, weight, graded)
        self.unit = unit               # integer
        self.number = number           # integer
        self.assignments = assignments # object []

    def __repr__(self):
        return f'{self.course} Standard {self.unit}.{self.number}: {self.name}'

# A standard will be made up of several assignments
class Assignment(Category):

    def __init__(self, name, course, average, points, weight, graded, unit, standard):
        super().__init__(name, course, average, points, weight, graded)
        self.unit = unit                # integer
        self.standard = standard        # integer

    def __repr__(self):
        return f'{self.course} - Assignment {self.unit}.{self.standard}: {self.name}'


