# -*-encoding: utf-8-*-
import random

'生成随机打折码'


def generateRandomCode():
    return random.randrange(1, 501)


#
# def checkList(list, num):
#     for i in range(0, len(list)):
#         list.

dict1 = {}  # 10
dict2 = {}  # 50
dict3 = {}  # 140
# 字典实现
while (len(dict3) < 140):
    num = generateRandomCode()
    if ((not dict1.has_key(num)) and len(dict1) < 10):
        dict1[num] = num
    if ((not dict2.has_key(num)) and (not dict1.has_key(num)) and len(dict2) < 50):
        dict2[num] = num
    if ((not dict2.has_key(num)) and (not dict1.has_key(num)) and (not dict3.has_key(num)) and len(dict3) < 140):
        dict3[num] = num

# 列表实现
list1 = []
list2 = []
list3 = []
while (len(list3) < 140):
    num = generateRandomCode()
    if ((list1.count(num) <= 0) and len(list1) < 10):
        list1.append(num)
    if ((list1.count(num) <= 0) and (list2.count(num) <= 0) and len(list2) < 50):
        list2.append(num)
    if ((list1.count(num) <= 0) and (list2.count(num) <= 0) and (list3.count(num) <= 0) and len(list3) < 140):
        list3.append(num)

list = list1 + list2 + list3

# 元组实现
tuple = (generateRandomCode(),)
while len(tuple) < 200:
    num = generateRandomCode()
    if (tuple.count(num) <= 0):
        tuple1 = (num,)
        tuple = tuple1 + tuple


print "字典元素有：", len(dict1)
print "列表元素有:", str(list)
print "元组:", len(tuple)

input1 = input('请输入您抽中的券的号码: ')  #
if (list1.count(input1) > 0):
    print "您可以买打5折的啦！"
elif (list2.count(input1) > 0):
    print "您可以买打8折的啦！"
elif (list3.count(input1) > 0):
    print "您可以买打9.5折的啦！"
else:
    print '很遗憾您的号码没有中奖。'
