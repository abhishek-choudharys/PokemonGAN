import os
from PIL import Image

src = "resizedData"
dest = "resized_RGB"

os.mkdir(dest)

for i in os.listdir(src):
    img = Image.open(os.path.join(src, i))

    if img.mode == 'RGBA':
        img.load()
        bg = Image.new("RGB", img.size, (0,0,0))
        bg.paste(img, mask = img.split()[3]) #we paste img into the alpha channel
        bg.save(os.path.join(dest, i.split('.')[0] + '.jpg'), 'JPEG')
    else:
        img.convert('RGB')
        img.save(os.path.join(dest,i.split('.')[0] + '.jpg'), 'JPEG')
