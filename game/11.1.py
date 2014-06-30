#coding=utf-8

class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "生的"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiments) > 0:
            msg = msg + " 和"
        for i in self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + " ."
        return msg


    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "烤焦"
        elif self.cooked_level > 5:
            self.cooked_string = "烤熟"
        elif self.cooked_level > 3:
            self.cooked_string = "半熟"
        else:
            self.cooked_string = "生的"


    def addCondiment(self, condiment):
        self.condiments.append(condiment)

myDog = HotDog()
print myDog
print "Cooking hot dog for 4 minutes"
myDog.cook(4)
print myDog
print "cook hot dog for 3 more minutes"
myDog.cook(3)
print myDog
print "What happens if I cook it for 10 more minutes?"
myDog.cook(10)
print myDog
print "Now , i'm going to add some stuff on my hot dog"
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
print myDog


'''
myDog = HotDog()
print "现在热狗进行4分钟的烘烤"
myDog.cook(4)#传递cook方法 参数是4
print myDog.cooked_string
print myDog.condiments
'''