import os


def path(directory):
    try:
        os.chdir(directory)
        return os.getcwd()
    except FileNotFoundError:
        print("Error: directory not found please check if it's exists")
