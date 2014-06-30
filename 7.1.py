#coding=utf-8
'''这是for循环
num = input('输入您想了解数字的乘法表 输入100则为1-9乘法表')
print '您的乘法表如下:'
if num == 100 :
    for i in range(1,10,1):
        for k in range(1,10,1):
            print i ,'x',k,'=', i * k
else:
    for w in range(1,10,1):
        print num , 'x' , w ,'=' , num * w
'''
'''这是while循环
num = input('输入您想了解数字的乘法表 输入100则为1-9乘法表')
print '您的乘法表如下:'
k = 1
j = 1
if num == 100:
    while k < 10 :
        while j < 10:
            print k ,'x',j,'=',k * j
            j = j + 1
            if j == 10 :
                j = 1
                k = k + 1
                break
while k < 10 :
    print num , 'x', k ,'=',k * num
    k = k + 1
'''
'''for循环版本
num = input('需要计算乘法的数字')
high = input('最大的被乘数')
print '您的乘法表'
for k in range(1,high+1,1):
    print num , 'x' , k , '=' , num * k
'''
'''
num = input('需要计算乘法的数字')
high = input('最大的被乘数')
w = 1
while w < high+1 :
    print num , 'x' , w , '=' , num * w
    w = w + 1
'''