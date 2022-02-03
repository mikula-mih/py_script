import sys, os, time
import math
import random, re
from pynput.keyboard import Key, Controller

'''
def shift_n(rep, delay):
    kb = Controller()
    a = Key.shift
    b = 'n'
    while rep:
        rep -= 1
        with kb.pressed(a):
            kb.press(b)
            time.sleep(delay)
            kb.release('n')
    time.sleep(delay)


kb =Controller()
time.sleep(3)
shift_n(5, 1)
'''
# for i in range(5):
#     k = random.randint(0, 10)
#     print(k)

# print('"C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"')
# runas /user:mikeBrave_01 "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

a = os.getlogin()
import subprocess

# p1 = subprocess.Popen('runas /user:mikeBrave_01 "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"')

#p1.stdin.write(('8598').encode())

# p1.communicate(('8598').encode())
# p2 = subprocess.run('echo 8598', capture_output=True, input=p1.stdout, text=True)

#######################################################################################################################
# gmtime()
# localtime()

#calendar.timegm()
# mktime()

# time.strftime()

#time.strftime("%a, %d %b %Y %H:%M:%S", localtime())

t0 = time.time()
print(time.time())
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))

time.sleep(2.5)

T = time.time()
t1 = time.time()
print(T)
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
print(t1-t0)

totalAccounts_PC = int(math.pow(2, 12))
numPC = 0
index_start = numPC * totalAccounts_PC
index_end = index_start + totalAccounts_PC
print(hex(index_start))
userList = []
for i in range(index_start, index_end):
    userName = hex(i)
    userList.append(userName)

print(userList)

numHEX = ['0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
userList_NEW = []
for i in range(16):
    for j in range(16):
        for k in range(16):
            userName = f'0x{numPC}{numHEX[i]}{numHEX[j]}{numHEX[k]}'
            userList_NEW.append(userName)

print(userList_NEW)

print(time.time())
