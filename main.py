#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print as pt
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import MotorActions as MA
import Calibaration as Cal
import lightsensor

# Write your program here
brick.sound.beep()
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 50, 100)
ForwardSensor = UltrasonicSensor(Port.S1)
cSensor = ColorSensor(Port.S2)
LeftSensor = InfraredSensor(Port.S3)
lightSensor = lightsensor.CustomLight(Port.S4)
time = 0

def foundvictim():
    notes = [(523, 1000), (494, 1000), (440, 500), (330, 500),
    ("repeat", 5, 330), ("repeat", 3, 440), (440, 500), (392, 250), (440, 500), (349, 500)]
    #  brick.sound.beep(frequency=500, duration=100, volume=30)
    for note in notes:
        if note[0] == "repeat":
            for i in range(note[1]):
                brick.sound.beep(note[2], 125, 10)
                wait(125)
        else:
            brick.sound.beep(note[0], note[1], 10)

    brick.light(None)

def forward(stopdist):
    robot.drive(-1000, 0)
    stopdist = int(stopdist)
    while ForwardSensor.distance() > stopdist:
        wait(1)
    robot.stop()
    
def backward(time):
    #Working
    robot.drive(1000, 0)     
    wait(time)

def rightturn():
    #Working perhaps slightly off needs more precision testing
    left.run_time(-1000, 1311, Stop.BRAKE, False)
    right.run_time(1000, 1311, Stop.BRAKE, True)

def leftturn():
    #Working perhaps slightly off needs more precision testing
    left.run_time(1000, 1311, Stop.BRAKE, False)
    right.run_time(-1000, 1311, Stop.BRAKE, True)

def main():
    coords  = [0, 0]
    left.reset_angle(0); right.reset_angle(0)
    Kp, Ki, Kd, i, last_error, target = 20, 0, 0, 0, 0, 5
    conveyor_belt = Motor(Port.A)
    directions_made = []
    stopwatch = StopWatch(); stopwatch.resume()
    driving_forward = False
    while True:
        if stopwatch.time() >= 100000: #  OUR LAST HOPE FOR POINTS!!!!!
            robot.stop()
            if driving_forward:
                directions_made.append(("forward", stopwatch.time() - start_time))
            driving_forward = False
            break
        if lightSensor.refelctivity() <= 500:
            backward(1000)
        if cSensor.color() == Color.BLUE:
            robot.stop(Stop.BRAKE)
            if driving_forward:
                directions_made.append(("forward", stopwatch.time() - start_time))
            driving_forward = False
            conveyor_belt.run_time(-100, 1000, Stop.BRAKE, False)
            foundvictim()
        if LeftSensor.distance() >= 40:
            wait(500)
            robot.stop(Stop.BRAKE)
            if driving_forward:
                directions_made.append(("forward", stopwatch.time() - start_time))
            driving_forward = False
            leftturn(); directions_made.append("left turn")
            robot.drive_time(-1000, 0, 1000); directions_made.append(("forward", 1000))
        elif ForwardSensor.distance() <= 300:
            robot.stop(Stop.BRAKE)
            if driving_forward:
                directions_made.append(("forward", stopwatch.time() - start_time))
            driving_forward = False
            rightturn(); directions_made.append("right turn")
        else:
            robot.drive(-1000, 0)
            driving_forward, start_time = True, stopwatch.time()
    for direction in directions_made:
        if direction == "left turn":
            robot.stop()
            rightturn()
        elif direction == "right turn":
            robot.stop()
            leftturn()
        else:
            robot.drive_time(-1000, 0, direction[1])

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


#foundvictim()

robot.drive_time(-1000, 0, 1500)
wait(1000)
main()
'''
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
'''
