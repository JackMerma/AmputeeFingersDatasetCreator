from config import *
import os
from src.process.filter import *


def validate_source_type(src_type):

    if src_type == None:
        raise Exception(f"You must pass a source type file. {POST_RAISE_MESSAGE}")

    if src_type not in SOURCE_TYPE_OPTIONS:
        raise Exception(f"Invalid source type [{src_type}]. {POST_RAISE_MESSAGE}")


def validate_file_path(file_path):

    if not os.path.isfile(file_path):
        raise Exception(f"Invalid file path [{file_path}]. {POST_RAISE_MESSAGE}")


def get_aoi_limits():
    return AOI_MIN_RANGE, AOI_MAX_RANGE


def get_eoi_limits():
    return EOI_MIN_RANGE, EOI_MAX_RANGE


def label(image):
    # Applying filter for AOI
    aoi_min, aoi_max = get_aoi_limits()
    aoi_mask = mask(image, aoi_min, aoi_max)

    # Getting aoi position and boundingbox
    aoi_mask_middle_point, aoi_mask_boundingbox = get_middle_point_and_boundingbox(aoi_mask)
    print("middle point: ", aoi_mask_middle_point)
    print("bounding box: ", aoi_mask_boundingbox)
    show_image(aoi_mask, "img2")

    # Applying filter for EOI
    eoi_min, eoi_max = get_eoi_limits()
    eoi_mask = mask(image, eoi_min, eoi_max)
    #show_image(eoi_mask, "img3")
