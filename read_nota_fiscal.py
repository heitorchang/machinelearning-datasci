import pytesseract
from pytesseract import Output
import cv2
import numpy as np


def removeshadows(img):
    # https://stackoverflow.com/questions/44752240/how-to-remove-shadow-from-scanned-images-using-opencv
    rgb_planes = cv2.split(img)

    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    # result_norm = cv2.merge(result_norm_planes)

    return result

def readimg(fname):
    img = cv2.imread(fname)
    img = removeshadows(img)
    s = pytesseract.image_to_string(img) # , lang="por")

    return s
    
"""
# original code used in YouTube screen captures
def readimgdata(fname):
    img = cv2.imread(fname)
    
    d = pytesseract.image_to_data(img, output_type=Output.DICT, config="--psm 12")
    for k in d:
        print(k, d[k])

    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        if True:
            print(x, y, d['text'][i])
"""
