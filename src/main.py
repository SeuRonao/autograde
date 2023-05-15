"""Main entry point of the application"""

from setup import setup
from models.autograde import Autograde


def main():
    """Main function"""
    report = Autograde()
    report.update_submissions()
    report.grade_submissions()
    report.save()
    print("All done. Check the report folder for the results.")


if __name__ == "__main__":
    setup()
    main()
