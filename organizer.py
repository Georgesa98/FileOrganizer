import argparse
from core.utils import path
from core.methods import Organizer


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
        "-i",
        "--image",
        help="organize images only in the directory",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--video",
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
    parser.add_argument(
        "-t",
        "--text",
        help="organize text only in the directory",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-p",
        "--program",
        help="organize programs only in the directory",
        required=False,
        action="store_true",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    dir = path(args.directory)
    organizer = Organizer(dir)
    kwargs = args._get_kwargs()
    kwargs.pop(0)
    organize_all = True
    for key, value in kwargs:
        if value == True:
            organize_all = False
    if organize_all:
        organizer.organize()
    if args.image:
        organizer.organizerPhotos()
    if args.audio:
        organizer.organizeAudio()
    if args.compressed:
        organizer.organizeCompressed()
    if args.program:
        organizer.organizeProgram()
    if args.text:
        organizer.organizeText()


if __name__ == "__main__":
    main()
