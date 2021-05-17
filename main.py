import os
import sys
import requests
import random
from PIL import Image, ImageDraw, ImageFont

from get_quotes import get_quotes

def main():
    fdir = '/Users/neharavi/Desktop/good-morning/flowers/sunflower/'
    size = (500, 500)
    font_type = ImageFont.truetype('Arial.ttf', 10)
    f = random.choice(os.listdir('./flowers/sunflower'))

    author = get_quotes()[1]
    quote = get_quotes()[0]
    print('{0} FAMOUSLY SAID THAT {1}'.format(author, quote))

    if f.endswith('.jpg'):
        #imports input image
        im = Image.open(os.path.join(fdir, f))
        #prints input metadata
        print('filetype: {0}, size: {1}'.format(im.format, im.size))
        #extracts file name
        fn = os.path.splitext(f)[0]
        #resizes image
        im.thumbnail(size)
        #text
        draw = ImageDraw.Draw(im)
        draw.text(xy=(0,0), text=quote, fill=(0,0,0), font=font_type)
        #saves output image
        im.save('./out/{}.png'.format(fn))

if __name__ == "__main__":
    main()