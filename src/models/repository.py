"""
Module for the Repository class
"""

import subprocess
from pathlib import Path


class Repository:
    """
    Repository class is used to represent a repository.
    """

    def __init__(self, github_owner: str, repository_name: str, repository_path: Path):
        self.github_owner = github_owner
        self.repository_name = repository_name
        self.repository_path = repository_path
        self.repository_url = f"http://github.com/{github_owner}/{repository_name}"

    def clone(self):
        """
        Clone the repository.

        returns True if the repository is cloned successfully, False otherwise.
        """

        try:
            subprocess.run(["gh", "repo", "clone", f"{self.github_owner}/{self.repository_name}",
                            self.repository_path],
                           capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def pull(self):
        """
        Pull the repository.

        returns True if the repository is pulled successfully, False otherwise.
        """
        try:
            subprocess.run(["git", "pull"], cwd=self.repository_path, capture_output=True,
                           check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        except FileNotFoundError:
            return False
