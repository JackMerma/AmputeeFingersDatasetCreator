from config import *
from src.process.src import *
from src.gui.main import *


def main():

    # Getting parser
    args = load_parser()

    if args.process:
        process(src_type=args.type, file_path=args.file)
    else: # No args loads the user interface
        gui()


if __name__ == "__main__":
    main()
