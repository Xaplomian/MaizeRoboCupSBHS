#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 50, 100)
ForwardSensor = UltrasonicSensor(Port.S1)
cSensor = ColorSensor(Port.S2)
irSensor = InfraredSensor(Port.S3)

def forward(stopdist):
    robot.drive(-100, 0)
    stopdist = int(stopdist)
    while ForwardSensor.distance() > stopdist:
        wait(1)
        time += 1
    robot.stop()

def backward(time):
    #NOTTESTED
    robot.drive(100, 0)
    wait(time)

def rightturn():
    #NOTTESTED
    left(100, 10)
    right(-100, 10)

def leftturn():
    #NOTTESTED
    left(-100, 10)
    right(100, 10)


forward(200)

backward(time)

rightturn()
leftturn()

