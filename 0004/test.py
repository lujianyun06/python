# -*-encoding: utf-8-*-

'word statictis'


def is_letter(char):
    tmp = map(ord, char)[0]
    is_a_letter = False
    if (tmp >= 97 and tmp <= 122) or (tmp >= 65 and tmp <= 90):
        is_a_letter = True
    return is_a_letter


file_apple = open("apple")
is_word_end = True
word_count = 0
file_apple.seek(0, 2)
byte_size = file_apple.tell()
file_apple.seek(0, 0)
tmp = file_apple.read(1)

i = 0
while(i < byte_size):
    if ((is_word_end) and is_letter(tmp)):
        is_word_end = False
    elif ((not is_word_end) and (not is_letter(tmp))):
        is_word_end = True
        word_count += 1
    tmp = file_apple.read(1)
    i += 1
    if ((i == byte_size) and (not is_word_end)):
        word_count += 1

file_apple.close()

print word_count,
