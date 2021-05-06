from PIL import Image, ImageDraw, ImageFont
import os
import sys

def main():
    fdir = '/Users/neharavi/Desktop/good-morning/flowers/sunflower/'
    size = (500, 500)
    font_type = ImageFont.truetype('Arial.ttf', 30)
    for f in os.listdir('./flowers/sunflower'):
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
            draw.text(xy=(0,0), text='Good Morning', fill=(255,69,0), font=font_type)
            #saves output image
            im.save('./out/{}.png'.format(fn))
    
if __name__ == "__main__":
    main()