import os
import urllib.request
import random
from pathlib import Path
import cv2
import numpy as np


class DataUtils:
    def download_data(self, input_file, output_file, img_name):
        """ Download all images from an input file """
        data_urs = []
        with open(input_file, "r") as f:
            for line_n, line in enumerate(f):
                url = line.strip()
                urllib.request.urlretrieve(url, f'{output_file}/{img_name}_{line_n}.jpg')

    def color_filter(self, img):
        """ Adds a filter color to a given image """
        # openCV opens the image in order BGR (blue, green, red)

        blue = random.random()
        green = random.uniform(0, 1 - blue)
        red = 1 - blue - green  # sum up to 1 in order to keep the same intensity as in the original image

        img[:, :, 0] = img[:, :, 0] * blue
        img[:, :, 1] = img[:, :, 1] * green
        img[:, :, 2] = img[:, :, 1] * red
        return img

    def overlay_images(self, wazer_img, bg_img):
        """ Overlays the wazers on the background image """
        mask = np.array([wazer_img[:, :, 3], wazer_img[:, :, 3], wazer_img[:, :, 3]])
        y_offset = random.randint(0, bg_img.shape[0] - wazer_img.shape[0])
        x_offset = random.randint(0, bg_img.shape[1] - wazer_img.shape[1])

        bg_img[y_offset:y_offset + wazer_img.shape[0], x_offset:x_offset + wazer_img.shape[1]] = \
            bg_img[y_offset:y_offset + wazer_img.shape[0], x_offset:x_offset + wazer_img.shape[1]] + \
            wazer_img[:, :, 0:3]

        return bg_img

    def detect_edges(self):
        img = np.zeros((200, 200), dtype=np.uint8)
        img[50:150, 50:150] = 255
        # two possible ways: detect contours and Canny
        ret, thresh = cv2.threshold(img, 127, 255, 0)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        edges = cv2.Canny(img, 100, 200)

        pass


WAZERS_FILE = "wazer_urls.txt"

DATA_DIR = Path('data/users_wo_bg')
FILE_NAME = 'wazer'

if __name__ == '__main__':
    utils = DataUtils()

    ''' Process:
    1. go over all wazers
    2. color the wazers
    3. overlay the wazers on all different backgrounds
    '''
    # wazer_img = cv2.imread('wazer_1a.png', cv2.IMREAD_UNCHANGED)
    # bg_img = cv2.imread('app.jpg')
    # cv2.waitKey()
    # cv2.destroyAllWindows()
