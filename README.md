# Autograde

This script is used to autograde the assignments for any course using github classroom and autograding with github actions.

While github offers a nice 2k minutes of free compute time for private repos, it is often not enough for a course with 100+ students or a lot of activities.
While you could make all repositories public and have "infinite" minutes this way, this often is not an option for courses with sensitive data.

This script offers a simple way to clone all the students repositories, run the autograding and generate a grade report for all students.

## Dependencies

- [Python 3.6+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Github CLI](https://cli.github.com/)
- [Act](neckros.github.io/act/)
- [Docker](https://www.docker.com/) (because of act dependency)

## Usage

1. Install all dependencies.
2. Verify that dependencies where installed correctly

   1. Run `act --version`
   2. Run `gh --version`
   3. Run `docker --version`

   All of them must return something like `command --version` and not an error.

3. Configure github CLI with your credentials.
4. Configure act with the medium image.
5. Create a github classroom assignment and add the autograding workflow to it.
6. Download/clone this repository.
7. Edit the `config.ini` file to match your needs.
8. Create/Edit the `students.csv` file to match your students.
   You can download it from the github classroom rooster page.
   The file must contain the following columns: `identifier`,`github_username`, `github_id` and `name`.
9. Create/Edit the `exercise.csv` file to match your exercises.
   It must contain a single column `exercise` containing each prefix of each exercise defined when creating the classroom assignment.
10. Run `python3 src/main.py` to clone all repositories and run the autograding.
11. See the results in the `report` folder.

## Security

This script uses the github CLI to clone all repositories.
This means that you need to have access to all repositories.

This script uses [Act](https://github.com/nektos/act) to run the github actions.
While this is a great tool, it is not officially supported by github.
This means that it is possible that it will break in the future.

Act uses Docker to run the workflow, while this protects the host machine from malicious code, it is not perfect.

## Virtual Environment

you can use `pip install -r requirements.txt` to install all python dependencies in a virtual environment.
