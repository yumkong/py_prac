# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 12:08:35 2016

@author: yumkong
"""
#1 image filtering
#import Image, ImageFilter
#im = Image.open('v2.jpg')
##w, h = im.size
#im2 = im.filter(ImageFilter.EDGE_ENHANCE)
#im2.save('v2_edgeenhance.jpg','jpeg')

import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    #chr: change a ASCII code to a character
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.show()
image.save('code.jpg', 'jpeg');
