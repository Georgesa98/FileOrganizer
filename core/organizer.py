import argparse
from utils import path
from methods import organize


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
    parser.add_argument(
        "-a",
        "--all",
        help="organize the whole directory",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-i",
        "--images",
        help="organize images only in the directory",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--videos",
        help="organize videos only in the directory",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--compressed",
        help="organize compressed files only in the directory",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--audio",
        help="organize audio only in the directory",
        required=False,
        action="store_true",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    dir = path(args.directory)
    print(dir)


if __name__ == "__main__":
    main()
