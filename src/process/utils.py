from config import *
import os
import cv2
import json
from src.process.filter import *
from src.process.draw import *


def filter_images_and_videos(folder):
    image_ex = [".png", ".jpg", ".jpeg"]
    video_ex = [".mp4"]

    image_paths = []
    video_paths = []

    for file in os.listdir(folder):
        file_name, file_ex = os.path.splitext(file)

        if file_ex in image_ex:
            image_paths.append(file)

        if file_ex in video_ex:
            video_paths.append(file)

    return image_paths, video_paths


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


def save_json(data, file_name):
    json_object = json.dumps(data, indent=2)

    # Saving file
    completed_path = os.path.join(DATASETS_FOLDER, f"{file_name}.json")

    with open(completed_path, "w") as outfile:
        outfile.write(json_object)


def label(image, path):
    # Applying filter for AOI
    aoi_min, aoi_max = get_aoi_limits()
    aoi_mask = mask(image, aoi_min, aoi_max)

    # Getting aoi position and boundingbox
    aoi_mask_middle_point, aoi_mask_boundingbox = get_middle_point_and_boundingbox(aoi_mask)

    #bgr_image = swap_hsv2bgr(image)

    # Drawing middle point in the image
    #aoi_middle = draw_circle(bgr_image, aoi_mask_middle_point)

    # Drawing boundingbox in the image
    #aoi_boundinbox = draw_boundingbox(bgr_image, aoi_mask_boundingbox)

    # Applying filter for EOI
    #eoi_min, eoi_max = get_eoi_limits()
    #eoi_mask = mask(image, eoi_min, eoi_max)

    # Saving json file

    file_name, extension = os.path.splitext(os.path.basename(path))

    data = {
            "file_path": path,
            "file_name": file_name,
            "width": len(image),
            "height": len(image[0]),
            "aoi_data": {
                "middle_point": aoi_mask_middle_point,
                "boudingbox": aoi_mask_boundingbox
                }
            }
    save_json(data, file_name)
