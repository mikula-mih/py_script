import math, time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller as mController

#############################################################
kb = Controller()
mouse = mController()

# for i in range(10):
#     time.sleep(0.5)
#     print(mouse.position)

# (x, y) = (1919, 1079)
xMAX = 1919
yMAX = 1079
margin = 19

x0 = math.floor(xMAX/2)
y0 = math.floor(yMAX/2)
mouse.position = (x0, y0)
print(y0)

r = 200
# SNAPS = round((xMAX-2*margin)/move_x)

# for angle in range(360):
#     timeElapse = 5
#     # =1881 --> (1881 * timeElapse) = Duration
#     speed = timeElapse/360
#     time.sleep(speed)
#     move_x = round(math.sin(math.radians(angle))) * r
#     move_y = round(math.cos(math.radians(angle))) * r
#     # move_y = (0) * (-1)
#     # Coordinate Adjustment [1, -1]
#     mouse.move(move_x, move_y)


delta_Angle = math.ceil(math.degrees(6.28/360))
myCoordinates = []
for angle_turn in range(360):
    myAngle = math.radians(delta_Angle * angle_turn)
    # for circle
    x = math.cos(math.pi/2 - myAngle) * r
    y = math.sin(math.pi/2 - myAngle) * r

    myCoordinates.append([round(x), round(y)])

print(myCoordinates)

mouse.position = ((x0 + myCoordinates[0][0] * (1)), (y0 + myCoordinates[0][1] * (1)))
for i in range(359):
    timeElapse = 5
    time.sleep(timeElapse/360)
    X = myCoordinates[i+1][0] - myCoordinates[i][0]
    Y = myCoordinates[i+1][1] - myCoordinates[i][1]
    mouse.move(X, Y)

