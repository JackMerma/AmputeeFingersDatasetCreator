import cv2

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
    c1 = (x_min, y_min)
    c2 = (x_max, y_min)
    c3 = (x_max, y_max)
    c4 = (x_min, y_max)

    return ((x_max + x_min) // 2, (y_max + y_min) // 2), (c1, c2, c3, c4)
