import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt

import time


filenames = glob.glob("/home/mp913/Desktop/Louis/CLOTH/*.jpg")
filenames.sort()
images = [cv2.imread(img) for img in filenames]

count = 1
#display one by one with diff windows name

# for img in images:
#     imgname = 'Image {}'.format(count)
#     cv2.namedWindow(imgname, cv2.WINDOW_NORMAL)
#     cv2.imshow(imgname, img)
#     count +=1
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


#display continuosly with same windows name

# for img in images:
#     cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
#     cv2.imshow("Image", img)
#     cv2.waitKey(0)

#display infinite loop+ continously with same windows name

# while True:
#     cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
#     for img in images:
#         cv2.imshow("Image", img)
#         k = cv2.waitKey(0)
#
#         if k == 27:
#            break
#
#     if k == 27:
#         break


while True:
    count = 1
    cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

    for img in images:
        color = ('b', 'g', 'r')
        title = 'Image {}'.format(count)
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))
        plt.title(title, fontsize = 10)

        #First RGB color
        axs[0, 0].set_title("RGB Color")
        axs[0, 0].set_xlabel("Color Value")
        axs[0, 0].set_ylabel("Quantity")

        for i, col in enumerate(color):
            histr = cv2.calcHist([img], [i], None, [256], [0, 256])
            axs[0, 0].plot(histr, color=col)

        #Second histogram
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        axs[0, 1].set_title("Grayscale")
        axs[0, 1].hist(gray.ravel(), 256, [0, 256])


        #Third histogram
        axs[1, 0].set_title("Histogram")
        axs[1, 0].hist(img.ravel(), 256, [0, 256])


        #Fourth histogram
        axs[1, 1].set_title("Histogram")
        axs[1, 1].hist(img.ravel(), 256, [0, 256])
        axs[1, 1].remove()


        plt.show(False) #to allow code run below
        cv2.imshow("Image", img)

        k = cv2.waitKey(0)
        plt.close()

        count +=1
        if k == 27:
           break

    if k == 27:
        break
