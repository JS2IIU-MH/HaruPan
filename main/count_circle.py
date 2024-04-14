''' 画像の中の円を検出する '''

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

sample_file = 'OUT_IMG/20240408_121522504_iOS.jpg'

def find_circle(filename):
    ''' 画像の中の円を検出する, findContours版 '''
    # load file, Grayscale
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('OUT_IMG/00_sample.png', img)

    # filtering
    _, threshold = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

    # contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_DUPLEX

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, (0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) > 10:
            cv2.putText(img, 'circle', (x, y), font, 1, (0))
        
    cv2.imwrite('OUT_IMG/01_sample.png', img)

def find_circle_hough(filename):
    ''' 画像の中の円を検出する, HoughCircles版 '''

    # load file, Grayscale
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('OUT_IMG/00h_sample.png', img)

    img_dst = img.copy()

    # filtering
    # _, threshold = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

    # gaussian blur
    KERNEL_SIZE = 7
    kernel = KERNEL_SIZE * 2 + 1
    img_blur = cv2.GaussianBlur(img, (kernel, kernel), None)

    # canny edge detection
    CANNY_TH1 = 80
    CANNY_TH2 = 60
    img_edge = cv2.Canny(img_blur, threshold1=CANNY_TH1, threshold2=CANNY_TH2)
    cv2.imwrite('OUT_IMG/01h_sample.png', img_edge)

    # HoughCircles
    circles = cv2.HoughCircles(img_edge,
                               cv2.HOUGH_GRADIENT,
                               dp=1,
                               minDist=10,
                               param1=100,
                               param2=30,
                               minRadius=135,
                               maxRadius=160)
    
    # circles = np.unit16(np.around(circles))
    circles = np.int16(np.around(circles))

    font = cv2.FONT_HERSHEY_DUPLEX

    for circle in circles[0, :]:
        # draw circle
        cv2.circle(img_dst, (circle[0], circle[1]), circle[2], (255, 150, 255))
        cv2.putText(img_dst, 'circle', (circle[0], circle[1]), font, 1, (0))
    
    cv2.imwrite('OUT_IMG/02h_sample.png', img_dst)


def main():
    find_circle_hough(sample_file)

if __name__ == '__main__':
    main()
