import os
import cv2

src = "Pokemon_GAN/data"
dest = "resizedData"

os.mkdir(dest)

for i in os.listdir(src):
    img = cv2.imread(os.path.join(src, i))
    img = cv2.resize(img, (256, 256))
    cv2.imwrite(os.path.join(dest,i), img) #resized images are written in a new folder
