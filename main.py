#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 50, 100)
#ForwardSensor = UltrasonicSensor(Port.S1)
cSensor = ColorSensor(Port.S2)
LeftSensor = InfraredSensor(Port.S3)
time = 0

def forward(stopdist):
    robot.drive(-100, 0)
    stopdist = int(stopdist)
    while ForwardSensor.distance() > stopdist:
        wait(1)
    robot.stop()

def colourchecker():
    #Working now
    while 1 == 1:
        currentcol = cSensor.color()
        if currentcol == Color.BLUE:
            brick.sound.file(SoundFile.BLUE)
            print('Blue')
        elif currentcol == Color.BLACK:
            brick.sound.file(SoundFile.BLACK)
            print('Black')
        elif currentcol == Color.GREEN:
            brick.sound.file(SoundFile.GREEN)
            print('Green')
        elif currentcol == Color.YELLOW:
            brick.sound.file(SoundFile.YELLOW)
            print('Yellow')
        elif currentcol == Color.RED:
            brick.sound.file(SoundFile.RED)
            print('Red')
        elif currentcol == Color.BROWN:
            brick.sound.file(SoundFile.BROWN)
            print('Brown')
        elif currentcol == Color.WHITE:
            brick.sound.file(SoundFile.WHITE)
            print('White')
        else:
            brick.sound.file(SoundFile.BOING)
            print('fail')
        wait(5000)
    
def backward(time):
    #Working
    robot.drive(100, 0)     
    wait(time)

def rightturn():
    #Working perhaps slightly off needs more precision testing
    robot.drive_time(100, 90, 3100)

def leftturn():
    #Working perhaps slightly off needs more precision testing
    robot.drive_time(-100, -90, 3100)

#forward(200)
#brick.sound.beep()
#backward(2000)
#brick.sound.beep()
#rightturn()
#brick.sound.beep()
#leftturn()
#brick.sound.beep()
colourchecker()