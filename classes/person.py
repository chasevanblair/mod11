"""

Program: person.py

Author: Chase Van Blair

Last date modified: 7/14/20


The purpose of this program is to learn class inheritance by making a student class which is derived from the
person class

"""


class Person:
    """Person class"""

    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        """
        displays attributes of a person
        :return: listed attributes
        """
        return self._last_name + ", " + self._first_name + ":" + self._address


class Student(Person):
    """
    student class
    """
    def __init__(self, student_id, lname, fname, major="Computer Science", gpa=0.0, addy=""):
        super().__init__(lname, fname, addy)
        self._id = student_id
        self._major = major
        self._gpa = gpa

    def display(self):
        """
        displays attributes of a student
        :return: listed attributes
        """
        return self._last_name + ", " + self._first_name + ":(" + str(self._id ) + ") " + self._major + " gpa: " \
               + str(self._gpa)


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
