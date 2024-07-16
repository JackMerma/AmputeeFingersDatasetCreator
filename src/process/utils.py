from config import *
import os


def validate_source_type(src_type):

    if src_type == None:
        raise Exception(f"You must pass a source type file. {POST_RAISE_MESSAGE}")

    if src_type not in SOURCE_TYPE_OPTIONS:
        raise Exception(f"Invalid source type [{src_type}]. {POST_RAISE_MESSAGE}")


def validate_file_path(file_path):

    if not os.path.isfile(file_path):
        raise Exception(f"Invalid file path [{file_path}]. {POST_RAISE_MESSAGE}")
