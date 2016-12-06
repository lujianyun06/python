# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

PI = 3.14
Offset = 0.5
radius = 25


def drawCirclePixel(imgdraw, img):
    width, height = img.size
    for w in range(width):
        for h in range(height):
            if (w == 199 and h == 0):
                a = 10
            distance = caculateDistance(w, h, 174, 24)
            offset = (distance - radius)
            if (offset <= 0):
                imgdraw.point((w, h), fill='#ff0000')


def caculateDistance(x1, y1, x2, y2):
    x = math.pow((x1 - x2), 2)
    y = math.pow((y1 - y2), 2)
    return math.sqrt(x + y)


def clipCircle(imgdraw, img):
    width, height = img.size
    for w in range(width):
        for h in range(height):
            distance = caculateDistance(w, h, 100, 100)
            offset = (distance - 100)
            if (offset > 0):
                imgdraw.point((w, h), fill='#00000000')

image = Image.open('WechatIMG13.jpeg')
im = image.resize((200, 200))
im.convert('RGBA')
im2 = Image.new('RGBA', (200, 200), '#ffff')
im2.paste(im)
draw = ImageDraw.Draw(im2)
clipCircle(draw, im2)
# drawCirclePixel(draw, im2)
bbox = (150, 0, 200, 50)
draw.ellipse(bbox, '#f00')
font = ImageFont.truetype("Arial.ttf", 20)
num = '999+'
draw.text((155, 15), num, '#fff', font)
# im3 = Image.blend(im, im2, alpha=100)
im2.save("0011.png", 'png')
