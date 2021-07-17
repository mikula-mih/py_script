import sys, os, time
import random
from pynput.keyboard import Key, Controller

print('Hello world')
def wait(delay):
    # ...
    time.sleep(delay)
def enter(rep, delay):
    kb = Controller()
    while rep:
        kb.press(Key.enter)
        time.sleep(delay)
        kb.release(Key.enter)
        rep -= 1
    time.sleep(0.5)


userList = [1, 2, 3]
for i in range(len(userList)):
    if i < (len(userList)-1):
        print(userList[i+1])
    else:
        print(userList[i-(len(userList)-1)])

# 0,1,2