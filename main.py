#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import MotorActions as MA
import Calibaration as Cal

# Write your program here
brick.sound.beep()
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 50, 100)
ForwardSensor = UltrasonicSensor(Port.S1)
cSensor = ColorSensor(Port.S2)
LeftSensor = InfraredSensor(Port.S3)
time = 0

def foundvictim():
    notes = [(523, 1000), (494, 1000), (440, 500), (330, 500),
    ("repeat", 5, 330), ("repeat", 3, 440), (440, 500), (392, 250), (440, 500), (494, 500)]
    #  brick.sound.beep(frequency=500, duration=100, volume=30)
    for note in notes:
        if note[0] == "repeat":
            for i in range(note[1]):
                brick.sound.beep(note[2], 250)
        else:
            brick.sound.beep(note[0], note[1], 50)

    brick.light(None)

def forward(stopdist):
    robot.drive(-1000, 0)
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
    left.run_time(-1000, 1800, Stop.BRAKE, False)
    right.run_time(1000, 2000, Stop.BRAKE, True)

def leftturn():
    #Working perhaps slightly off needs more precision testing
    left.run_time(1000, 1380, Stop.BRAKE, False)
    right.run_time(-1000, 1380, Stop.BRAKE, True)

def backwardtest(diststop):
    robot.drive(1000, 0)
    while ForwardSensor.distance() > diststop:
        wait(1)
    robot.stop()


def main():
    left.reset_angle(0); right.reset_angle(0)
    Kp, Ki, Kd, i, last_error, target = 20, 0, 0, 0, 0, 5
    conveyor_belt = Motor(Port.A)
    conveyor_belt.run_time(-100, 1000)
    while True:
        if cSensor.color() and cSensor.color() != Color.WHITE:
            robot.stop()
            conveyor_belt.run_time(-100, 500, Stop.BRAKE, False)
            foundvictim()
        if LeftSensor.distance() >= 50:
            wait(500)
            robot.stop()
            leftturn()
            robot.drive_time(-1000, 0, 1000)
        elif ForwardSensor.distance() <= 200:
            robot.stop()
            rightturn()
        else:
            robot.drive(-1000, 0)

#forward(100)
#backwardtest(500)
#brick.sound.beep()
#foundvictim()
#leftturn()
#brick.sound.beep()
#MA.backward(2000)
#brick.sound.beep()
#MA.rightturn()
#brick.sound.beep()
#MA.leftturn()
#brick.sound.beep()
#colourchecker()

#Testing

wait(1000)
foundvictim()
main()
rightturn()
leftturn()
while True:
    if Button.UP in brick.buttons():
        brick.sound.beep()
        forward(200)
    elif Button.DOWN in brick.buttons():
        brick.sound.beep()
        backwardtest(200)
    elif Button.LEFT in brick.buttons():
        brick.sound.beep()
        leftturn()
    elif Button.RIGHT in brick.buttons():
        brick.sound.beep()
        rightturn()    
    else:
        brick.sound.file(SoundFile.SORRY)
    wait(500)  
