'''
main.py
code for the Rescue Robot for the Robocup Open Rescue competition
by James Treloar, Harry Wu, Cyril Subramanian, Kalaish Stanley
August 2019
Licensed under GNU GPLv3
'''

#!/usr/bin/env pybricks-micropython

#  Harry: I can't import pybricks for some reason
#  Cyril: Read https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf, you need some other stuff as well that I think only James has.
#  Cyril: If you don't have an ev3, just code here
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

'''
INITIALISING
'''
brick.sound.beep()
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 50, 100)

'''
+----X-Y----+
|W         Z| X = Color Sensor, points downwards
|           | Y = Forward Sensor, points directly forwards
|           | W = left Sensor, points at 45 deg to left
|           | Z = right Sensor, points at 45 def to right
|           | If U disagree a lot then comment somewhere 
+-----------+
'''
#We need two colour sensors remember.

leftSensor = None #UltrasonicSensor(Port.S1)
colorSensor = ColorSensor(Port.S2)
rightSensor = InfraredSensor(Port.S3)
forwardSensor = None #InfraredSensor(Port.S4)
time = 0
MAX_DUTY = 100

'''
FUNCTION DEFINITIONS
'''
#  Made changes so that the robot goes forward, and when something 
# in front of it, it stops and goes backwards the exact amount
def forward(stopdist):
    robot.drive(-100, 0)
    stopdist = int(stopdist)
    time_elapsed = 0
    while forwardSensor.distance() > stopdist:
        wait(1)
        time_elapsed += 1
    robot.stop()
    return time_elapsed

def colour_checker(): #  Functional function

    currentColor = colorSensor.color()
    if currentColor == Color.BLUE:
        brick.sound.file(SoundFile.BLUE)
        print('Blue')
    elif currentColor == Color.BLACK:
        brick.sound.file(SoundFile.BLACK)
        print('Black')
    elif currentColor == Color.GREEN:
        brick.sound.file(SoundFile.GREEN)
        print('Green')
    elif currentColor == Color.YELLOW:
        brick.sound.file(SoundFile.YELLOW)
        print('Yellow')
    elif currentColor == Color.RED:
        brick.sound.file(SoundFile.RED)
        print('Red')
    elif currentColor == Color.BROWN:
        brick.sound.file(SoundFile.BROWN)
        print('Brown')
    elif currentColor == Color.WHITE:
        brick.sound.file(SoundFile.WHITE)
        print('White')
    else:
        brick.sound.file(SoundFile.BOING) #  Boing
        print('fail')
    return currentColor
    
    
def backward(time): #  Functional function
    robot.drive(100, 0)     
    wait(time)

def rightturn(): #  Functional function but not precise
    robot.drive_time(100, 90, 3100)

def leftturn(): #  Functional function but not precise
    robot.drive_time(-100, -90, 3100)
def retreat():
    #drives straight back when it stalls or meets black tile.
    while robot.stalled() or colour_checker() == BLACK:
        brick.sound.beep(130, 500)
        robot.run_time(-100, 600)

def foundvictim():
    brick.light(color.RED)
    #plays the tune from 'Despacito'
    # Why? I have no idea.
    noteG = 196
    noteB = 247
    noteC = 261
    noteD = 293
    noteE = 330
    #brick.sound.beep(frequency=500, duration=100, volume=30)
    brick.sound.beep(noteG, 200, 50)
    for i in range(3):
        wait(20)
        brick.sound.beep(noteD, 200, 50)
    wait(20)
    brick.sound.beep(noteD, 420, 50)
    brick.sound.beep(noteE, 200, 50)
    wait(20)
    brick.sound.beep(noteE, 420, 50)
    brick.sound.beep(noteC, 630, 50)
    # last four notes
    wait(100)
    brick.sound.beep(noteD, 440, 75)
    brick.sound.beep(noteC, 440, 75)
    brick.sound.beep(noteB, 220, 80)
    brick.sound.beep(noteG, 220, 85)

    brick.light(None)

'''
TODO
• We must make a function that tells it to scan along the left-hand
side of the maze
• We must check out how to use our sensors and finalise sensor position
• Then, we use it to write a function to identify victims
AND to go there and beep.
• write function to give resources to identified victims

Finally, we can write function to make it more likely for robot to exit
at the entry position and earn bonus points there.
'''

'''driver code'''
# time_elapsed = forward(200)
# brick.sound.beep()
# backward(time_elapsed)
# brick.sound.beep()
# rightturn()
# brick.sound.beep()
# leftturn()
# brick.sound.beep()
# colour_checker()
