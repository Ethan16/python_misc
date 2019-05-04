# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: demo_pillow_letter_verification_code.py
@time: 2019/4/26 下午10:19
@description: 
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rnd_char():
    char = chr(random.randint(65, 90))
    print('[Debug]char: '+char)
    return char


def rnd_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# [done]:OSError: cannot open resource
# font = ImageFont.truetype('Arial.ttf', 36)
# [done]对于字体是有要求的。deepin默认带的字体就不能正常显示。如下的字体可以正常显示。
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())

for t in range(4):
    draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())
    # draw.text((10, 25), rnd_char(), font=font, fill=rnd_color2())

image = image.filter(ImageFilter.BLUR)
image.save('verification_code.jpg', 'jpeg')
