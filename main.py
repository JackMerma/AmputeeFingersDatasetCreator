from config import *
from src.process.src import *


def main():

    # Getting parser
    args = load_parser()

    if args.process:
        process(src_type=args.type, file_path=args.file)


if __name__ == "__main__":
    main()
