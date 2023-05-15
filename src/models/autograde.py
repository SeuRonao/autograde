"""
This module contains the Autograde class, which is the main class of the application.
"""

from pathlib import Path
import pandas as pd
from models.submission import Submission
from config import config


class Autograde:
    """
    Autograde class is used to represent the autograding.
    """

    def __init__(self):
        # Stores the result of the autograding
        student_file_location = Path(
            config['DEFAULT']['student_file_location']).resolve()
        self.data = pd.read_csv(student_file_location, encoding="utf-8", dtype={
            "identifier": "string",
            "github_username": "string",
            "github_id": "string",
            "name": "string"})

        # Stores the exercises prefixes
        exercise_file_location = Path(
            config['DEFAULT']['exercise_file_location']).resolve()
        self.exercises = pd.read_csv(exercise_file_location,
                                     encoding="utf-8", dtype="string")
        self.exercises = pd.Series(self.exercises["exercise"].values)

        # Add the exercises columns to the data
        for row in self.exercises:
            self.data[f"{row}-repo"] = pd.Series(dtype="string")
            self.data[f"{row}-grade"] = pd.Series(dtype="int")
            self.data[f"{row}-max"] = pd.Series(dtype="int")
            self.data[f"{row}-points"] = pd.Series(dtype="float")

        # Populates the submission dictionary based on the students and exercises
        self.submissions: dict[str, Submission] = {}
        clone_folder_location = Path(
            config['DEFAULT']['clone_folder_location']).resolve()
        available_students = self.data["github_username"].dropna()
        owner = config['DEFAULT']['owner']
        for username in available_students:
            for exercise in self.exercises:
                submission = Submission(username, owner,
                                        exercise,
                                        clone_folder_location / f"{exercise}-{username}")
                self.submissions["-".join([exercise, username])] = submission

    def update_submissions(self):
        """
        Update the submissions.
        """
        done = 1
        for submission in self.submissions.values():
            print(
                f"Updating submission {done} of {len(self.submissions)}: "
                f"{submission}", end=" ", flush=True)
            if submission.update():
                print("✅")
            else:
                print("❌")
            done += 1

    def grade_submissions(self):
        """
        Grade the submissions.
        """
        done = 1
        for submission in self.submissions.values():
            print(
                f"Grading submission {done} of {len(self.submissions)}: "
                f"{submission}", end=" ", flush=True)
            grade = submission.grade()
            if grade.max_grade == 0:
                print(grade, "❌")
            else:
                print(grade, "✅")
            done += 1

            # Find the row of the student corresponding to this submission
            username = submission.github_username
            exercise_prefix = submission.exercise_prefix
            self.data.loc[self.data["github_username"] == username, [
                f"{exercise_prefix}-repo",
                f"{exercise_prefix}-grade",
                f"{exercise_prefix}-max",
                f"{exercise_prefix}-points"]] = [
                    submission.repository.repository_url,
                    grade.grade,
                    grade.max_grade,
                    grade.points]

    def save(self):
        """
        Save the data to the report folder.
        """
        report_folder_location = Path(
            config['DEFAULT']['report_folder_location']).resolve()
        self.data.to_csv(report_folder_location / "report.csv",
                         encoding="utf-8", index=False)

    def __str__(self):
        return f"{self.data}"
