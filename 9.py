#coding=utf-8
'''
friends = []
friends.append('David')
print friends
friends.append('Many')
print friends

print friends[1] #获取列表的内容
print friends[1:2]  #获取列表的分片
append() #向末尾增加一个元素
extend() #向末尾增加多个元素
insert() #在列表的某个位置增加一个元素

remove() #删除元素 根据元素内容
del() #删除元素 根据元素位置
pop() #取出一个元素并交给你

in # if 'a' in friends 查询friends里是否有 a 这个内容
friends.index('a') #查找friends里的a 在那个位置

sort() #列表排序
reverse #列表排逆序

namelist = []
for a in range(0,5,1):
    name = raw_input('enter name : \t')
    namelist.append(name)
print 'name is ',
for w in range(0,5):
    print namelist[w],

namelist = []
for a in range(0,5,1):
    name = raw_input('enter name : \t')
    namelist.append(name)
print 'name is ',
namelist.sort()
for w in range(0,5):
    print namelist[w],

namelist = []
for a in range(0,5,1):
    name = raw_input('enter name : \t')
    namelist.append(name)
b = input('选择序号')
print namelist[b]

'''
namelist = []
for a in range(0,5,1):
    name = raw_input('enter name : \t')
    namelist.append(name)
b = raw_input('想要删除?')
c = raw_input('替换成新?')
d = namelist.index(b)
del namelist[d]
namelist.insert(d,c)
print namelist