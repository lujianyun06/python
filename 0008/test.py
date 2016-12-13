#-*-encoding:utf-8-*-
import os
import line
work_path = "/Users/ljy/PycharmProjects/l6J6y/0008/file"
file_name = 'test.html'

def find_body(file_name):
    h5_file = open(file_name)
    in_body = False
    cache = ""
    tmp = h5_file.readline()
    while "" != tmp:
        if("<body" in tmp):
            in_body = True
            cache += tmp
        elif(in_body and not("</body>" in tmp)):
            cache += tmp
        elif (in_body and ("</body>" in tmp)):
            in_body = False
            cache += tmp
        tmp = h5_file.readline()
    return cache

os.chdir(work_path)
body = find_body(file_name)
line_count = line.find_lines_func2(file_name)

print body
print '共有：', line_count, '行'


