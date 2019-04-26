# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: demo_pillow_blur.py
@time: 2019/4/24 下午10:27
@description: 
"""

from PIL import Image, ImageFilter

im = Image.open('meinv.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('meinv_blur.jpg', 'jpeg')