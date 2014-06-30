#coding=utf-8
#import urllib
#file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
#message = file.read()
#print message
#answer = raw_input()
#print type(answer)
#a = int(raw_input())
#print a
#print type(a)
a = input()
if a == 1 :
    xm = raw_input('请输入姓')
    mz = raw_input('请输入名')
    print xm,mz
if a == 2:
    c = input('请输入房屋长度,单位是米')
    k = input('请输入房屋宽度,单位是米')
    j = input('每平方尺的地毯价格')
    print c * k ,'面积平方米'
    cc = c * k * 9
    print cc ,'平方尺'
    print cc * j ,'人民币'
if a == 3:
    w = input('你有多少五分钱')
    e = input('你有多少二分钱')
    r = input('你有多少一分钱')
    print '你拥有:', w * 0.05 + e * 0.02 + r * 0.01