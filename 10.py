#coding=utf-8

def printMyaddress():
    print '武汉'
    print 'Hubei'
    print 'hanyang abc'


printMyaddress()


def printMyaddress(myname,city):
    print myname
    print myname
    print city
    print 'hanyang abc'


printMyaddress('Millyn','wuhan')


def calculateTax(price, Tax_rate):
    taxTotal = price + (price * Tax_rate)
    my_price = 10000 #global my_price 使my_price强制变为全局变量
    print "my_price(inside function) = ", my_price
    return taxTotal

my_price = float(raw_input('Enter a price:'))

totalPrice = calculateTax(my_price,0.06)
print "print = ", my_price , "Total price = " , totalPrice
print "my_price(outside function)  = ",my_price


def myadd(name,add,add1,city,city1,zip,com):
    print name,
    print add,
    print add1,
    print city,
    print city1,
    print zip,
    print com,
b = []
for a in range(0,7,1):
    c = raw_input('依次输入名、地址、街道、城市、省市、邮编、国家')
    b.append(c)

myadd(b[0],b[1],b[2],b[3],b[4],b[5],b[6])


def calculateTax(price, Tax_rate):
    taxTotal = price + (price * Tax_rate)
    global my_price
    my_price = 10000 #global my_price 使my_price强制变为全局变量
    print "my_price(inside function) = ", my_price
    return taxTotal

my_price = float(raw_input('Enter a price:'))

totalPrice = calculateTax(my_price,0.06)
print "print = ", my_price , "Total price = " , totalPrice
print "my_price(outside function)  = ",my_price




def money(five,two,one):
    print '五分钱有:',five * 0.05
    print '两分钱有:',two * 0.02
    print '一分钱有:',one * 0.01
    print '总共有:',five * 0.05 + two *0.02 +one *0.01

b = []
for a in range(0,3):
    c = input('依次输入五分钱数量、两分钱数量、一分钱数量')
    b.append(c)

money(b[0],b[1],b[2])
