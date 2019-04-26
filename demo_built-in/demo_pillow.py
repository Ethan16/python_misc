# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@sina.com
@file: demo_pillow.py
@time: 2019/4/14 下午8:33
@description: 
"""

from PIL import Image

im = Image.open('xiaoqiao.jpg')

w, h = im.size
print('Original size : %sx%s' % (w, h))

print(int(h/2))
im.thumbnail((w//2, h//2))
print('Resize image to : %s x %s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')