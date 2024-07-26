import cv2
import os
import matplotlib.pyplot as plt
from config import *


def read_image(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image


def write_image(image, file_path):
    cv2.imwrite(file_path, image)


def show_image(image, file_name=TESTING_FILE_NAME):
    image_path = os.path.join(DATASETS_FOLDER, f"{file_name}.{TESTING_FILE_EXTENSION}")
    cv2.imwrite(image_path, image)

    # Showing the image using open command
    os.system(f"open {image_path}")


def swap_hsv2bgr(image):
    new_image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    return new_image


def draw_circle(image, point, color = MAIN_PIXEL_COLOR):
    new_image = image.copy()

    # Drawing the point
    cv2.circle(new_image, point, radius=7, color=color, thickness=-1)
    return new_image


def draw_boundingbox(image, points, color = MAIN_PIXEL_COLOR):
    new_image = image.copy()
    p1, p2, p3, p4 = points
    thickness = 7

    # Drawing points
    cv2.line(new_image, p1, p2, color, thickness=thickness)
    cv2.line(new_image, p2, p3, color, thickness=thickness)
    cv2.line(new_image, p3, p4, color, thickness=thickness)
    cv2.line(new_image, p4, p1, color, thickness=thickness)

    return new_image
