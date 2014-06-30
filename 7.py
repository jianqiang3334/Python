#coding=utf-8
for looper in [1, 2, 3, 4, 5]:
    print "hello"

for looper1 in [1, 2, 3, 4 ,5]:
    print looper1 , "time 8 = " , looper1 * 8


for looper2 in range (1, 5):
	print looper2, "time 8 = " , looper2 *8

for looper3 in range(1, 11):
	print looper3 ,"time 8 = " , looper3 * 8

import time
for i in range (10 , 0 , -1):
	print i
	time.sleep(1)
	print "BLAST OFF!"

for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
	print cool_guy, "is the coolest guy ever"

print "Type 3 to countinue, anything else to quit."
someInput = raw_input()
while someInput == '3':
	print "Thank you for the 3 . very king of you"
	print "Type 3 to countinue , anything else to quit."
	someInput = raw_input()
print "That's not 3, so i'm quitting now"

for i in range (1,6) :
	print
	print 'i = ', i ,
	print 'Hello, how',
	if i == 3:
		continue
	print 'are you today?'

#continue 是提前跳出循环的函数 但他并不会终止循环 只是跳出该循环的下一步 重头开始


for i in range (1,6) :
	print
	print 'i = ', i ,
	print 'Hello, how',
	if i == 3:
		break
	print 'are you today?'

#break 是直接跳出循环，就此终止循环过程。