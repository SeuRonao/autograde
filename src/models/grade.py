"""
This module defines the Grade class, which contains the grade and max_grade of a grade.
"""


class Grade:
    """
    Grade class is used to represent a grade.
    """

    def __init__(self, grade: int, max_grade: int):
        self.grade = grade
        self.max_grade = max_grade

    @property
    def points(self) -> float:
        """
        Returns the points of the grade.
        """
        if self.max_grade == 0:
            return 0
        return self.grade / self.max_grade * 100

    def __str__(self):
        if self.max_grade == 0:
            return "(Not Graded)"
        return f"{self.grade}/{self.max_grade} ({self.points:.1f}%)"
