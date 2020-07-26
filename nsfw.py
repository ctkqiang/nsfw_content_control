#!/usr/bin/env python3.8
import os
import glob
from PIL import Image


def get_picture_skin_ratio(im):
    im = im.crop((int(im.size[0]*0.2), int(im.size[1]*0.2),
                  im.size[0]-int(im.size[0]*0.2), im.size[1]-int(im.size[1]*0.2)))
    skin = sum([count for count, rgb in im.getcolors(im.size[0]*im.size[1]) if rgb[0] > 60 and rgb[1]
                < (rgb[0]*0.85) and rgb[2] < (rgb[0]*0.7) and rgb[1] > (rgb[0]*0.4) and rgb[2] > (rgb[0]*0.2)])
    return float(skin)/float(im.size[0]*im.size[1])


def main():
    for image_dir in ('porn', 'clean'):
        for image_file in glob.glob(os.path.join('assets/nsfw/nude/', "*.png")):
            skin_percent = get_picture_skin_ratio(Image.open(image_file)) * 100
            if skin_percent > 30:
                logcat('?nude::true, ', 'porn {0} exposed {1:.0f}% skin'.format(
                    image_file, skin_percent))
            else:
                logcat('?nude::false,', 'CLEAN {0} exposed {1:.0f}% skin'.format(
                    image_file, skin_percent))


def logcat(x, y):
    return print(x, y)


if __name__ == '__main__':
    main()
