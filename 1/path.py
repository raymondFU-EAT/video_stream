import os
import numpy as np
import cv2


path = 'D:/雷蒙/1/123'
all = os.listdir(path)
with open('D:/雷蒙/1/1.txt', 'w') as fs:
    for f in all:
        fs.write(f+',')
        print(f)
#
# ./db/609/det/IMG_1081-1-1.jpg

with open('D:/雷蒙/1/1.txt', 'r') as fs:

    li = fs.read().split(',')[:-1]
    print(li)
    for i in range(len(li)):
        image = cv2.imread('123/'+li[i])

        cv2.imshow("123", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(li[i])


# img = cv2.imread(i)
