class Student:
   
    def __init__(self,firstName = None ,lastName = None,id = None):
        if (not firstName ) and (not lastName) and (not id):
            self.firstName = ""
            self.lastName = ""
            self.id = 0
            self.__major ='CS'
        else:
            self.firstName = firstName
            self.lastName = lastName
            self.id = id
            self.__major  ='EE'
        self.tests = []
        self.grade = ''

    def add_grade(self,score):
        self.tests.append(score)

    def compute_grade(self):
        sum = 0
        for score in self.tests:
            sum = sum + score
        avg = sum / len(self.tests)
        if avg > 90:
            grade = 'A'
        elif avg > 85:
            grade = 'A-'
        elif avg > 80:
            grade = 'B'
        else:
            grade = 'B'
        return grade

    def add_grade(self,score):
        self.tests.append(score)

    def compute_grade(self):
        sum = 0
        for score in self.tests:
            sum = sum + score
        avg = sum / len(self.tests)
        if avg > 90:
            grade = 'A'
        elif avg > 85:
            grade = 'A-'
        elif avg > 80:
            grade = 'B'
        else:
            grade = 'B'
        return grade

    def __str__(self): #toString version of python :)
        return 'id: ' + str(self.id) + ' First name: ' + self.firstName + ' Last Name: ' +self.lastName + ' Major: '+ self.__major
        + ' grade: ' + self.grade