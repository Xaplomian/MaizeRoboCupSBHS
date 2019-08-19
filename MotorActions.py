from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 50, 100)
ForwardSensor = UltrasonicSensor(Port.S1)
cSensor = ColorSensor(Port.S2)
LeftSensor = InfraredSensor(Port.S3)

def forward(stopdist):
    robot.drive(-100, 0)
    stopdist = int(stopdist)
    while ForwardSensor.distance() > stopdist:
        wait(1)
    robot.stop()

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