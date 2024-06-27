import argparse
from utils import path


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="File Organizer",
        description="this script is used to organize files in a directory in a simple and good way",
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="directory of files you want to organize",
        required=True,
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    dir = path(args.directory)
    print(dir)


if __name__ == "__main__":
    main()
