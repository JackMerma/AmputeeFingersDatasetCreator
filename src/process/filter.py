import cv2
import os
import matplotlib.pyplot as plt
from config import *

def read_image(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image


def show_image(image):
    image_path = os.path.join(DATASETS_FOLDER, f"{TESTING_FILE_NAME}.{TESTING_FILE_EXTENSION}")
    cv2.imwrite(image_path, image)

    # Showing the image using open command
    os.system(f"open {image_path}")


def mask(image, min_range, max_range):
    print(image.shape)
    print(min_range)
    print(max_range)
    mask = cv2.inRange(image, min_range, max_range)
    return mask
