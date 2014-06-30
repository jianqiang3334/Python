#coding=utf-8
box = input('您油箱的大小,单位(升)')
size = input('您油箱目前百分比,填写数字')
km = input('每升油可以行驶多少km')
a = box * size / 100 * km
print '您还可以行驶:' ,a ,'Km'
if a > 200 :
    print '您可以继续前行到下个加油站再进行加油'
else:
    print '您无法继续前行到下个加油站请就地加油'