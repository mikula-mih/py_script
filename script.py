import sys, os, time
import random
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller

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

#############################################################

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(mouse.position))
wait(1.0)
print(mouse.position)
# x - 1919 y - 1079
wait(1)
mouse.scroll(0, 10)
print(mouse.position)
'''
# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)
'''