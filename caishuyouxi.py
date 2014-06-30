#coding=utf-8
import random
secret = random.randint(1, 100)
guess = 0
tries = 0

print '这是一个可爱的猜数游戏,系统会从1-100随机生成神秘数字,你有6次机会输入自己的答案竞猜'
print '每次输入答案后系统会提示大或小于神秘数字,一起来玩游戏吧!'

while guess != secret: #进行while循环,等guess不等于secret时
    guess = input("请输入你的答案")
    if guess < secret:
        print "数字太小拉!"
    elif guess > secret:
        print "数字太大拉!"
    tries = tries + 1 #失去一次竞猜机会
    if guess == secret:
        print "恭喜你答对了!"
    if tries == 6:
        print "很遗憾你已经用完6次机会,少侠请重新来过吧!正确答案是:", secret
