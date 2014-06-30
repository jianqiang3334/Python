#coding=utf-8
'''
num = int(raw_input('请输入数字'))
for a in range (1,num + 1 ):
    print '*',

num1 = int(raw_input('请输入数字'))
for a1 in range (0,num1):
    print '*',

numblock = int(raw_input('你需要排列几次'))
numline = int(raw_input('你需要几行'))
numstatr = int (raw_input('每行需要多少 '))
for block in range(0 , numblock):
    for line in range(0, numline):
        for statr in range(0, numstatr):
            print '*',
        print
    print

numblock = int(raw_input('how many block of stars do you want?'))
for block in range(1,numblock +1):
    print 'block = ', block
    for line in range(1,block * 2):
        for star in range(1,(block + line ) * 2 ):
            print '*',
        print 'line = ', line , 'star = ', star
    print

dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 40
oni_cal = 20

print "\tDog \tBun \tKetchup \tMustard \tOnione \tCalories"
count = 1

for dog in [0,1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onione in [0,1]:
                    total_cal = dog_cal * dog + bun_cal * bun + ket_cal * ketchup + mus_cal * mustard + oni_cal * onione
                    print "#", count ,"\t",
                    print dog, "\t" , bun ,"\t", ketchup ,"\t",
                    print mustard,"\t",onione,
                    print "\t", total_cal
                    count = count +1

for i in range(5):
    for j in range(3):
        print "*",

'''
import time
a = input("Countdown timer : how many seconds?" )
for i in range(a,0,-1):
    print i,
    for j in range(i,0,-1):
        print '*',
    time.sleep(1)
    print
print "BLAST OFF"