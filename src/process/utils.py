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

    if os.path.exists(folder):
        for file in os.listdir(folder):
            file_name, file_ex = os.path.splitext(file)

            if file_ex in image_ex:
                image_paths.append(file)

            if file_ex in video_ex:
                video_paths.append(file)

    return image_paths, video_paths


def convert_video_to_images(base_path, file):

    completed_path = os.path.join(base_path, file)
    new_images = []

    # Reading video file
    cap = cv2.VideoCapture(completed_path)
    if not cap.isOpened():
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Converting to frames and saaving as images
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Generating file path
        video_file_name, _ = os.path.splitext(file)
        frame_file_name = f"{video_file_name}{frame_count}.png"
        frame_file = os.path.join(base_path, frame_file_name)
        new_images.append(frame_file_name)

        # Saving the file
        cv2.imwrite(frame_file, frame)
        frame_count += 1

    cap.release()

    return new_images


def get_processed_files_paths():

    paths = []

    COMPLETED_TEMP_PATH = os.path.join(UPLOAD_FOLDER_BASE, TEMP_FOLDER)

    if os.path.exists(COMPLETED_TEMP_PATH):
        for path in os.listdir(COMPLETED_TEMP_PATH):
            paths.append(os.path.join(TEMP_FOLDER, path))
    
    return paths


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
    
    if not os.path.exists(DATASETS_FOLDER):
        os.makedirs(DATASETS_FOLDER)

    json_object = json.dumps(data, indent=2)

    # Saving file
    completed_path = os.path.join(DATASETS_FOLDER, f"{file_name}.json")

    with open(completed_path, "w") as outfile:
        outfile.write(json_object)


def label(image, path, m_aoi=True, bb_aoi=True):
    # Applying filter for AOI
    aoi_min, aoi_max = get_aoi_limits()
    aoi_mask = mask(image, aoi_min, aoi_max)

    # Getting aoi position and boundingbox
    aoi_mask_middle_point, aoi_mask_boundingbox = get_middle_point_and_boundingbox(aoi_mask)

    bgr_image = swap_hsv2bgr(image)


    result_image = bgr_image.copy()

    # Writting middle point in the image
    if m_aoi:
        result_image = draw_circle(result_image, aoi_mask_middle_point)

    # Writting boundingbox in the image
    if bb_aoi:
        result_image = draw_boundingbox(result_image, aoi_mask_boundingbox)

    # Applying filter for EOI
    #eoi_min, eoi_max = get_eoi_limits()
    #eoi_mask = mask(image, eoi_min, eoi_max)

    # Saving processed image in the temp/ folder
    file_name, extension = os.path.splitext(os.path.basename(path))

    COMPLETED_TEMP_PATH = os.path.join(UPLOAD_FOLDER_BASE, TEMP_FOLDER)

    if not os.path.exists(COMPLETED_TEMP_PATH):
        os.makedirs(COMPLETED_TEMP_PATH)

    write_image(result_image, os.path.join(COMPLETED_TEMP_PATH, f"{file_name}.AOI{extension}"))

    # Saving json file
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
