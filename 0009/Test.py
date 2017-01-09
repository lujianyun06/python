#-*-encoding:utf-8-*-
'''
find link in a html file
'''
import os

def count_link(f_name):
    pass
    fhtml = open("test.html", "r")
    storged_lines = ""

    line = fhtml.readline()
    while line != "":
        line = line.strip()
        if "<link" in line:
            storged_lines += line + '\n'
        line = fhtml.readline()
    return storged_lines

os.chdir("/Users/ljy/PycharmProjects/work/")
print os.getcwd()
link_lines = count_link("test.html")
print link_lines



