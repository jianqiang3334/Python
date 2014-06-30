#coding=utf-8
sex = raw_input('请输入您的性别 男用m 女用f')
if  sex == 'm' :
    print ('对不起 我们只需要女孩子')
else:
    age = input('请输入您的年龄')
    if age >= 10 and age <= 12 :
        print ('你可以加入球队')
    else:
        print ('对不起,由于你的年龄无法加入球队')