from PIL import Image

import os
import cv2


def imgcrop(input, xPieces, yPieces):

    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)

    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces

    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)

            try:
                a.save(filename
                       + file_extension)

            except:
                pass


path = 'D:/雷蒙/cut_white/'
all = os.listdir(path)
for f in all:
    if f == 'cut':
        continue
    print(f)
    imgcrop(f, 1, 1)


#

# import cv2
# img = cv2.imread('IMG_1081.jpg')
# height, width, channels = img.shape
# print(height/2, width/2, channels)


# print(img.shape)
# print(type(img))

# cropped_1 = img[0:int(height/2), 0:int(width/2)]
# cropped_4 = img[int(height/2):int(height), int(width/2):int(width)]
# cropped_2 = img[0:int(height/2), int(width/2):int(width)]
# cropped_3 = img[int(height/2):int(height), 0:int(width/2)]
# n=2
# n=n*n
# cv2.imshow('cropped_1', cropped_4)
# for i in range(n+1):
# cv2.imwrite(f'cropped_{i+1}.jpg',f'{cropped_{i+1}}')
# print(i)
# cv2.imwrite('cropped_1.jpg', cropped_1)
# cv2.imwrite('cropped_2.jpg', cropped_2)
# cv2.imwrite('cropped_3.jpg', cropped_3)
# cv2.imwrite('cropped_4.jpg', cropped_4)
# cv2.waitKey(0)
