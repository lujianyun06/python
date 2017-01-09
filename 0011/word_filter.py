#-*-encoding:utf-8-*-
'''
words filter
'''
free = 'Freedom'
right = 'HuamnRights'

def replace_n():
    pass
    for i in range(0, len(keywords)):
        keywords[i] = keywords[i].replace('\n', '')

def check_word(str):
    pass
    for i in range(0, len(keywords)):
        # keywords[i] = keywords[i].decode("utf-8")
        if str in keywords[i]:
            print free
            return
    print right

def replace_word(str):
    pass
    for i in range(0, len(keywords)):
        keyword = keywords[i]
        if keyword in str:
            stars = len(keyword.decode('utf-8')) * '*'
            a = str.replace(keyword, stars)
            print a
            return


file_txt = open("filtered_words.txt")

keywords = file_txt.readlines()
replace_n()

str = raw_input()
replace_word(str)
