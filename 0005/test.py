#-*-encoding: utf-8-*-
'make a directory\'s pictures into iphone5 resolution'
from PIL import Image
import os.path

work_dir = '/Users/ljy/PycharmProjects/work'
png_postfix = '.png'
w_Iphone5 = 640
h_Iphone5 = 1136


def switch_pic_to_correct_size(pic):
    pass
    width_pic = pic.size[0]
    height_pic = pic.size[1]
    if (width_pic > w_Iphone5):
        width_pic = w_Iphone5
    if (height_pic > h_Iphone5):
        height_pic = h_Iphone5
    return (width_pic, height_pic)


print os.getcwd()
os.chdir(work_dir)

pic_name_list = []
pic_prename_list = []

a = os.walk(work_dir)

for dirpath, subdirnames, filenames in os.walk(os.getcwd()):
    print filenames
    for filename in filenames:
        if (filename.endswith('.png')) or (filename.endswith('.jpeg')):
            pic_name_list.append(filename)
            if filename.endswith('.png'):
                pic_prename_list.append(filename.partition('.png')[0])
            elif filename.endswith('.jpeg'):
                pic_prename_list.append(filename.partition('.jpeg')[0])
    print pic_name_list
    print pic_prename_list


for i in range(0, len(pic_name_list)):
    file =  Image.open(pic_name_list[i]).convert()
    new_size = switch_pic_to_correct_size(file)
    file = file.resize(new_size)   #注意了！resize是产生一个新的指定尺寸的image， 原来的没变，所以应该把新产生的赋给原来的
    file.save(pic_prename_list[i] + '_converted.png')
    print file.size





