import numpy as np
import cv2 as cv

square_len = 10
max_sobel_sum = 75


def calculate_sobel_sum(img_name):

    img = cv.imread(img_name)

    height, width, color_count = img.shape

    sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
    sobel = np.ceil(np.sqrt(sobel_x * sobel_x + sobel_y * sobel_y))

    sobel_sum = np.ceil(np.sqrt((sobel * sobel).sum(axis=2)))
    for x in range(height):
        for y in range(width):
            sobel_sum[x][y] = 1 if sobel_sum[x][y] > max_sobel_sum else 0
    return sobel_sum


def get_mask_of_squares(mask):
    height, width = mask.shape
    mask_of_squares = np.ones_like(mask)


    for i in range(height - square_len):
        for j in range(width - square_len):
            all_pixels_are_good = 1
            for x in range(i, min(height, i + square_len)):
                if all_pixels_are_good == 0:
                    break
                for y in range(j, min(width, j + square_len)):
                    if mask[x][y] == 1:
                        all_pixels_are_good = 0
                        break
            if all_pixels_are_good:
                for x in range(i, min(height, i + square_len)):
                    for y in range(j, min(width, j + square_len)):
                        mask_of_squares[x][y] = 0
    return mask_of_squares


def apply_filter_on_image(img, mask):
    height, width, color_count = img.shape
    img_copy = np.copy(img)
    for x in range(height):
        for y in range(width):
            if mask[x][y] == 1:
                img_copy[x][y] = [0, 0, 0]
    return img_copy
