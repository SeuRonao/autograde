"""Setup script for the project"""

import subprocess
import sys


def check_act():
    """Check if act is available"""
    try:
        subprocess.run(["act", "--version"],
                       capture_output=True, check=True)
        print("act is available")
    except subprocess.CalledProcessError:
        print("act is not available")
        print("Please install act from https://github.com/nektos/act")
        sys.exit(1)


def check_docker():
    """Check if docker is available"""
    try:
        subprocess.run(
            ["docker", "--version"], capture_output=True, check=True)
        print("docker is available")
    except subprocess.CalledProcessError:
        print("docker is not available")
        print("Please install docker from https://docs.docker.com/get-docker/")
        sys.exit(1)


def check_github_cli():
    """Check if github cli is available"""
    try:
        subprocess.run(
            ["gh", "--version"], stdout=subprocess.PIPE, check=True)
        print("github cli is available")
    except subprocess.CalledProcessError:
        print("github cli is not available")
        print("Please install github cli from https://cli.github.com/")
        sys.exit(1)


def setup():
    """Setup the project"""
    print("🧐 Checking dependencies 🧐")
    check_act()
    check_docker()
    check_github_cli()
    print("✅ Dependencies checked ✅")
