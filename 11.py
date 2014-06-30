#coding=utf-8
'''
class Ball:
    def bounce(self):
        if self.direction == "down": #当下面使用类时,bounce == down 所以会执行下面的语句 把direction 转换为 up
            self.direction = "up"


myBall = Ball()
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"

print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "Now i'm going to bounce the ball"
print
myBall.bounce() #使用一个类,即为class里的类.
print "now the ball's direction is ,",myBall.direction


class Ball:
    def __init__(self, color, size, direction): #初始化方法
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball("red","small","down") #对接__init方法
print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "Now i'm going to bounce the ball"
print
myBall.bounce()
print "now the ball's direction is ,",myBall.direction

class Ball:
    def __init__(self, color, size, direction): #初始化方法
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = "hi, i'm a " + self.size + " " + self.color + " ball!"
        return msg

myBall = Ball("red","small","down")
print myBall
'''

