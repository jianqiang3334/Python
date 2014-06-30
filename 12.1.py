#coding=utf-8

def c_to_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

celsius = float(raw_input('请输入华氏温度:'))
fahrenheit = c_to_f(celsius)
print '摄氏度:',fahrenheit

