#coding=utf-8
money = input('请输入结账金额')
if money <= 10 :
    print '您的折扣是10%'
    print '打折后您的消费是:' , money * 0.9
else:
    print '您的折扣是20%'
    print '打折后您的消费是:' , money * 0.8