#coding=utf-8
import easygui

easygui.msgbox('Hi,这是一款记录您邮递地址的软件请按照提示输入个人信息')
name = easygui.enterbox('请输入您的名字')
add = easygui.enterbox('请输入您的地址')
city = easygui.enterbox('请输入您的城市')
zip = easygui.enterbox('请输入您的邮政编码')
easygui.msgbox(name +'\n'+add +'\n'+city +'\n'+zip)