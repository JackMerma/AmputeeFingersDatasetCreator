import argparse
import numpy as np


SOURCE_TYPE_OPTIONS = ["img", "video"]
POST_RAISE_MESSAGE = "Use '--help' for more information."
DATASETS_FOLDER = "datasets"
TESTING_FILE_NAME = "test_image"
TESTING_FILE_EXTENSION = "png"

# Area Of Interest Limits (AOI)
AOI_MIN_RANGE = (36, 100, 25)
AOI_MAX_RANGE = (86, 255, 255)

# Element Of Interest Limist (EOI)
EOI_MIN_RANGE = (88, 20, 190) # 90-20-25
EOI_MAX_RANGE = (110, 255, 255)

MAIN_PIXEL_COLOR = (0, 0, 255) # Red in BGR


def load_parser():
    parser = argparse.ArgumentParser(description="Amputee Finger Dataset Creator description...")

    # General options
    parser.add_argument('-p', '--process', action="store_true", help="create data labeling")

    # Source type
    parser.add_argument('-t', '--type', type=str, required=False, help="define source type to process. Options:\n[img] for single image file\n[video] for video files")

    # File location
    parser.add_argument('-f', '--file', type=str, required=False, help="define source file path.")

    return parser.parse_args()
