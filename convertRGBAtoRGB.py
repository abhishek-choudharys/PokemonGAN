import os
from PIL import Image

src = "resizedData"
dest = "resized_RGB"
dest2 = "WGAN/resized_RGB"

os.mkdir(dest)

for i in os.listdir(src):
    img = Image.open(os.path.join(src, i))

    if img.mode == 'RGBA':
        img.load()
        bg = Image.new("RGB", img.size, (0,0,0))
        bg.paste(img, mask = img.split()[3]) #we paste img in bg using alpha channel as mask
        bg.save(os.path.join(dest, i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg, split dest at '.' and take first split
        bg.save(os.path.join(dest2, i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg, split dest at '.' and take first split
    else:
        img.convert('RGB')
        img.save(os.path.join(dest,i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg
        img.save(os.path.join(dest2,i.split('.')[0] + '.jpg'), 'JPEG') #save the images as jpeg
