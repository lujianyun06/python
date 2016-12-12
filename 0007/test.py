#-*-encoding: utf-8-*-
import os
import sys
work_path='/Users/ljy/PycharmProjects/l6J6y/0007/test'

'find how many lines written'

def find_lines_func1(filename):
    file = open(filename)
    file.seek(0, 2)
    char_size = file.tell()
    file.seek(0)
    line_count = 0
    for i in range(0, char_size + 1):
        char = file.read(1)
        if((char == '\n') or (char == '\r')): #最后一行是"" 空字符，但是使用'\0' 也无法匹配，只有用''才能匹配，可能理解为，
            # 就算一个空的文件也会有那个默认的第一行，但那个第一行是不算在字符中的。
            # 但文件里面确实有，但是用tell就读不到，只能用tell()+1强行多读一个字符作为补充
            line_count += 1
    return line_count

def find_lines_func2(filename):
    file = open(filename)
    lines = file.readlines() #可以看出，最后一个回车，确实不算。
    return len(lines)
    pass

def find_lines_func3(filename):
    file = open(filename)
    line_count = 0
    comment_lines_count = 0
    blank_lines_count = 0
    multi_comment_flag = False

    tmp = file.readline();
    while ("" != tmp):
        line_count += 1
        if ((tmp.lstrip()).startswith("//") and (not multi_comment_flag)):
            comment_lines_count += 1
        elif (len(tmp) == 1 and (not multi_comment_flag)):
            blank_lines_count += 1;
        elif ((tmp.lstrip()).startswith("/*")):
            multi_comment_flag = True
            comment_lines_count += 1
        elif ((tmp.lstrip()).startswith("*") and (multi_comment_flag)): #去除左边的空格 lstrip
            comment_lines_count += 1
        elif (tmp.endswith("*/\n") and (multi_comment_flag)):
            multi_comment_flag = False
            comment_lines_count += 1
        tmp = file.readline();
    return line_count, comment_lines_count, blank_lines_count


os.chdir(work_path)
if (os.getcwd() != '/Users/ljy/PycharmProjects/l6J6y/0007/test'):
    print "目录不对"
    os._exit()
pass
lines_count = 0
comments_count = 0
blank_count = 0
for parent, dirnames, filenames in os.walk(work_path):
    for i in range(0, len(filenames)):
        filename = filenames[i]
        # lines_count += find_lines_func1(filename)
        # lines_count += find_lines_func2(filename)
        tmp = find_lines_func3(filename)
        lines_count += tmp[0]
        comments_count += tmp[1]
        blank_count += tmp[2]

str = u"共有总行数:%d行, 其中注释有:%d行, 空白行有:%d行"%(lines_count, comments_count, blank_count)
print str
sys.exit()



