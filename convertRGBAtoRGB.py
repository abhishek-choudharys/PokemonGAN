import argparse
parser = argparse.ArgumentParser(description='Choose dest')

parser.add_argument('--type', dest='type', type=str, default='WGAN', help='choose destination folder')

args = parser.parse_args()
params = vars(args)

import os
import cv2

dest = "WGAN/resized_RGB"

if params['type'] == 'WGAN':
    dest = "WGAN/resized_RGB"
elif params['type'] == 'GAN':
    dest = "GAN/resized_RGB"
   

import os
from PIL import Image

src = "resizedData"

os.mkdir(dest)

for i in os.listdir(src):
    img = Image.open(os.path.join(src, i))

    if img.mode == 'RGBA':
        img.load()
        bg = Image.new("RGB", img.size, (0,0,0))
        bg.paste(img, mask = img.split()[3]) #we paste img in bg using alpha channel as mask
        bg.save(os.path.join(dest, i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg, split dest at '.' and take first split
        #bg.save(os.path.join(dest2, i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg, split dest at '.' and take first split
    else:
        img.convert('RGB')
        img.save(os.path.join(dest,i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg
        #img.save(os.path.join(dest2,i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg
