#-*-encoding:utf-8-*-
'''
make verification code pic
'''
from PIL import Image, ImageDraw, ImageFont
import random, os


def draw_rectangle(image, draw):
    image_w = image.size[0]
    image_h = image.size[1]
    for hi in range(0, image_h):
        for wi in range(0, image_w):
            # color = random.Random.randint(146, 210)
            color = random.randint(146, 210)
            draw.point((wi, hi), (color, color, color))
    pass

def draw_text(image, draw):
    image_w = image.size[0]
    image_h = image.size[1]
    font = ImageFont.truetype("qs.ttf", 25)
    for i in range(0, 4):
        num = str(random.randint(0,9))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        w = 30 + i * 40
        draw.text((w,20), num, color, font)



image = Image.new("RGB", (200, 50), "#fff")

draw = ImageDraw.Draw(image)
draw_rectangle(image, draw)
draw_text(image, draw)


image.save("code.png", "PNG")
