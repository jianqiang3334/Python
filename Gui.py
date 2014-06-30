#coding=utf-8
import easygui, random

secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("""Hi,这是一款用Python制作的猜数字游戏
系统会从1-99中随机抽取
你有六次机会进行答题!""")
while guess != secret and tries < 6:
    guess = easygui.integerbox('请输入你竞猜的数字')
    if not guess : break
    if guess < secret :
        easygui.msgbox(str(guess)+ '你的数字太小拉')
    elif guess > secret :
        easygui.msgbox(str(guess)+ '你的数字太大拉')
    tries = tries + 1

if guess == secret:
    easygui.msgbox('恭喜你答对题目!')
else:
    easygui.msgbox('少侠六次机会已经用完请重新来过')
