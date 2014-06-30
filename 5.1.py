#coding=utf-8
import easygui
easygui.msgbox('Hi,这是一款温度转换程序,可以把华氏温度转换成摄氏度')
wd = easygui.integerbox('请输入华摄氏度')
fuck = str((wd-32) * 5 / 9)
easygui.msgbox('当前温度: ' + fuck + '摄氏度')