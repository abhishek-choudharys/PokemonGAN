'''
Running instructions:

To use the small dataset:
run resize.py --dataset 1

To use the much larger dataset:
run resize.py --dataset 2

'''

import argparse
parser = argparse.ArgumentParser(description='Choose dataset')

parser.add_argument('--dataset', dest='dataset', type=int, default=2, help='choose dataset folder')

args = parser.parse_args()
params = vars(args)

import os
import cv2

if params['dataset'] == 1:
    src = "Pokemon_GAN/data"
elif params['dataset'] == 2:
    src = 'pokemon'

dest = "resizedData"

os.mkdir(dest)

for i in os.listdir(src):
    img = cv2.imread(os.path.join(src, i))
    img = cv2.resize(img, (256, 256))
    cv2.imwrite(os.path.join(dest,i), img) #resized images are written in a new folder
