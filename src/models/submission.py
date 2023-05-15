"""
This file contains the Submission class.
"""

import subprocess
import re
from pathlib import Path

from models.grade import Grade
from models.repository import Repository


class Submission:
    """
    Submission class is used to represent a submission.
    """

    def __init__(self, github_username: str, github_owner: str, exercise_prefix: str,
                 destination_folder: Path):
        """
        Initialize the submission.

        Args:
            github_username (str): Github alias of the submission
            github_owner (str): Github owner of the submission
            github_repo_name (str): Github repo name of the submission
            destination_folder (Path): Destination folder of the submission as a Path object
        """
        repository_name = f"{exercise_prefix}-{github_username}"
        self.repository = Repository(
            github_owner, repository_name, destination_folder)
        self.github_username = github_username
        self.exercise_prefix = exercise_prefix

    def update(self):
        """
        Update the submission by cloning if it is not cloned, or pulling if it is cloned.

        returns True if the submission is updated successfully, False otherwise.
        """

        cloned = self.repository.clone()
        if cloned:
            return True
        # Cloning can be false if the repository already exists.
        pulled = self.repository.pull()
        # Pulling can be false if the repository is not cloned because it does not exists.
        return pulled

    def grade(self):
        """
        Grade the submission.

        returns the grade object.
        """
        if not self.repository.repository_path.exists():
            return Grade(0, 0)

        result = subprocess.run(["act"], cwd=self.repository.repository_path,
                                capture_output=True, check=False)
        output = result.stdout.decode("utf-8")
        points = re.search(r"::set-output:: Points=(\d+)/(\d+)", output)

        return Grade(int(points.group(1)), int(points.group(2)))

    def __str__(self):
        return f"Submission(name={self.repository.repository_name})"

    def __repr__(self):
        return f"Submission(name={self.repository.repository_name})"
