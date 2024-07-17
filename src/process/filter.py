import cv2
import os
import matplotlib.pyplot as plt
from config import *

def read_image(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image


def show_image(image, file_name=TESTING_FILE_NAME):
    image_path = os.path.join(DATASETS_FOLDER, f"{file_name}.{TESTING_FILE_EXTENSION}")
    cv2.imwrite(image_path, image)

    # Showing the image using open command
    os.system(f"open {image_path}")


def mask(image, min_range, max_range):
    mask = cv2.inRange(image, min_range, max_range)
    return mask


def get_middle_point_and_boundingbox(image):
    x_min = -1
    x_max = -1
    y_min = -1
    y_max = -1

    # Iterating each pixel and getting mins and maxs
    for i in range(len(image)):
        for j in range(len(image[i])):
            x_min = j if x_min == -1 and image[i][j] == 255 else (j if image[i][j] == 255 and j < x_min else x_min)
            x_max = j if x_max == -1 and image[i][j] == 255 else (j if image[i][j] == 255 and j > x_max else x_max)
            y_min = i if y_min == -1 and image[i][j] == 255 else (i if image[i][j] == 255 and i < y_min else y_min)
            y_max = i if y_max == -1 and image[i][j] == 255 else (i if image[i][j] == 255 and i > y_max else y_max)

    # Creating coordinates for bounding box limits
    c1 = (y_min, x_min)
    c2 = (y_max, y_max)

    return ((y_max + y_min) // 2, (x_max + x_min) // 2), (c1, c2)
