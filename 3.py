#coding=utf-8
print '1为AA计算器,2为华氏温度转摄氏度,3为行程时间计算,4为矩形面积计算'
a = input('请选择本次程序')
if a == 1:
    money = input('本次用餐费用')
    xf = input('小费金额')
    rs = input('用餐人数')
    print '每人应承担:', (money + xf) / rs
if a == 2:
    wd = input('现在华氏温度?')
    ss = (wd - 32) * 5 / float(9)
    print ss,'摄氏度'
if a == 3:
    gl = input('请输入公里数')
    sd = input('请输入每小时行驶公里')
    print '本次行驶到目的地需要:',gl / sd ,'小时', (gl % sd),'分钟'
if a == 4:
    c = input('请输入长度')
    k = input('请输入宽度')
    print c * k ,'个平方'

