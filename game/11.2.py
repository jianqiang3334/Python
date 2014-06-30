#coding=utf-8
class BankAccount:
    def __init__(self): #这是一个类的属性
        self.bank_id = 'Millyn'
        self.bank_cood = '622023202030389562'
        self.bank_money = 100000.25
        self.bank_moneybak = 0
        self.bank_xz = 0 #此属性判断取钱或者存钱
        self.bank_change = [] #此属性打印存取钱反馈文字

    def __str__(self):  #这是一个查看类属性的方法
        msg = '您的姓名:'+self.bank_id + '\n您的卡号:'+ self.bank_cood + '\n您的余额:' + str(self.bank_money)  #打印银行基本信息
        msg = msg + '\n' + self.bank_change #打印从cook()返回的参数 从而判断存取钱 并打印信息
        msg = msg + '\n变动后余额:' + str(self.bank_moneybak)
        return msg

    def cook(self, xz): #判断从方法调用回的参数是 存钱还是取钱
        self.bank_xz = self.bank_xz + xz #使返回的参数适应到类属性里
        if self.bank_xz == 2:
            self.bank_change = '您现在存入了10000元至账户'
            self.bank_moneybak = self.bank_money + 10000
        elif self.bank_xz == 1:
            self.bank_change = '您现在取出了10000元至账户'
            self.bank_moneybak = self.bank_money - 10000
        else:
            print 'error'
class InterestAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.bank_lx = 1.5
        self.bank_time = 0
        self.bank_lx1 = 0
        self.bank_fk = []

    def addinterest(self,time):
        BankAccount.__init__(self)
        self.bank_time = self.bank_time + time
        self.bank_lx1 = self.bank_money * 0.015 * time
        self.bank_money = self.bank_money + self.bank_money * 0.015 * time

    def __str__(self):
        msg = '您的利息:' + str(self.bank_lx1)
        msg = msg + '\n总额为:' + str(self.bank_money)
        return msg

bankinfo = BankAccount()
bankinfo.cook(2)
print bankinfo

lixi = InterestAccount()
lixi.addinterest(12)
print lixi