#-*-encoding: utf-8-*-
import os
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
    while ("" != file.readline()):
        line_count += 1
    return line_count


os.chdir(work_path)
if (os.getcwd() != '/Users/ljy/PycharmProjects/l6J6y/0007/test'):
    print "目录不对"
    os._exit()
pass
lines_count = 0
for parent, dirnames, filenames in os.walk(work_path):
    for i in range(0, len(filenames)):
        filename = filenames[i]
        # lines_count += find_lines_func1(filename)
        # lines_count += find_lines_func2(filename)
        lines_count += find_lines_func3(filename)

print lines_count



