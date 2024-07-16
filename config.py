import argparse


SOURCE_TYPE_OPTIONS = ["img", "video"]
POST_RAISE_MESSAGE = "Use '--help' for more information."


def load_parser():
    parser = argparse.ArgumentParser(description="Amputee Finger Dataset Creator description...")

    # General options
    parser.add_argument('-p', '--process', action="store_true", help="create data labeling")

    # Source type
    parser.add_argument('-t', '--type', type=str, required=False, help="define source type to process. Options:\n[img] for single image file\n[video] for video files")

    # File location
    parser.add_argument('-f', '--file', type=str, required=False, help="define source file path.")

    return parser.parse_args()
