'''
main.py
code for the Rescue Robot for the Robocup Open Rescue competition
by James Treloar, Harry Wu, Cyril Subramanian, Kalaish Stanley
August 2019
Licensed under GNU GPLv3
'''

#!/usr/bin/env pybricks-micropython

#  Harry: I can't import pybricks for some reason
'''
Cyril: Read https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf, 
you need some other stuff as well that I think only James has.
Cyril: If you don't have an ev3, just code here
'''
#  Cyril: Also the code for turning left and right shouldn't work, I shall comment my suggestion code
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
directions_made = []

'''
+----X-Y----+
|W         Z| X = Color Sensor, points downwards
|           | Y = Forward Sensor, points directly forwards
|           | W = left Sensor, points at 45 deg to left
|           | Z = right Sensor, points at 45 def to right
|           | If U disagree a lot then comment somewhere 
+-----------+
'''
#  We need two colour sensors remember.

leftSensor = None #  UltrasonicSensor(Port.S1)
colorSensor = ColorSensor(Port.S2)
rightSensor = InfraredSensor(Port.S3)
forwardSensor = None #  InfraredSensor(Port.S4)
time = 0
MAX_DUTY = 100

'''
FUNCTION DEFINITIONS
'''
stopwatch = Stopwatch()
stopwatch.pause()
stopwatch.reset()

def calibrate():
    left.reset_angle(0); right.reset_angle(0)
    
def forward(stopdist): #  Functional
    global directions_made
    stopdist = int(stopdist)
    stopwatch.resume()
    robot.drive(-100, 0)
    while forwardSensor.distance() > stopdist:
        wait(1)
    time_elapsed = stopwatch.time()
    stopwatch.pause(); stopwatch.reset()
    robot.stop()
    if directions_made:
        direction, time = directions_made[-1]
        if direction == "back":
            if time > time_elapsed:
                directions_made[-1][-1] -= time_elapsed
            elif time < time_elapsed:
                del directions_made[-1]
                directions_made.append((direction, time_elaped - time))
            else:
                del directions_made[-1]
        elif direction == "forward":
            directions_made[-1] += time_elapsed
            
        

def colour_checker(): #  Functional

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
    robot.stop()

def rightturn(): #  Testing required
    robot.drive_time(100, 90, 3100)
    left.run(-100)
    right.run(100)
    wait(500); #  Further calculations required
    left.stop(); right.stop()

def leftturn(): #  Testing required
    left.run(100)
    right.run(-100)
    wait(500) #  Further calculations required with time
    left.stop(); right.stop()
def retreat():
    #  Drives straight back when it stalls or meets black tile.
    if robot.stalled() or colour_checker() == color.BLACK:
        robot.drive(100, 0)
        while robot.stalled() or colour_checker() == color.BLACK:
            wait(1)
        robot.stop()

def foundvictim():
    brick.light(color.RED)
    #plays the tune from 'Despacito'
    # Why? I have no idea.
    #  HARRY REALLY?!?!?!
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
    
def pid_wall_follow():
    dist = leftSensor.distance()
    kp, ki, kd, i, last_error = 1, 0, 0, 0, 0
    target_val = 100 #  in mm, can adjust if needed
    p = (target_value - dist)
    i += p
    d = p - last_error
    u = (p*kp + i*ki + d*kd)
    if u > 50:
        u = 50
    elif u < -50:
        u = -50
    left.run(-50 - u)
    right.run(-50 + u)
    
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
#  calibrate()
#  pid_wall_follow()
#  forward(200)
#  brick.sound.beep()
#  backward(2000)
#  brick.sound.beep()
#  rightturn()
#  brick.sound.beep()
#  leftturn()
#  brick.sound.beep()
#  colour_checker()
