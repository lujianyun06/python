from PIL import Image

im = Image.open('WechatIMG16.jpeg')
im2 = im.resize((600, 800))
im2.save('test.png', 'PNG')