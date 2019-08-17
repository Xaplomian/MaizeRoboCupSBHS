from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

#  Notes:

'''
Tile Types:
Silver: checkpoint
Black: No-go
Perhaps the silver tiles will return the value 'color.None'
'''

'''
+--Z-X-Y----+
|W         Z| X = Downward Color Sensor (Port.S4, still need to get)
|           | Y = Forward Ultrasonic Sensor (Port.S1)
|           | W = Left Infrared Sensor, points at 45 deg to left (Port.S3)
|           | Z = Forward Color Sensor (Port.S2)
|           | Disagrements can go into the following suggestion box: https://images.homedepot-static.com/productImages/704006ac-aea7-47ca-ad08-48d62bedf38e/svn/rubbermaid-plastic-trash-cans-2008186-64_1000.jpg
+-----------+ (or in comments, preferrably the suggestions box)
'''

brick.sound.beep()
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 50, 100)
ForwardSensor = UltrasonicSensor(Port.S1)
cSensor = ColorSensor(Port.S2)
LeftSensor = InfraredSensor(Port.S3)
TileDetector = None #  ColorSensor(Port.S4)
time = 0

def foundvictim(): #  *sigh* Thanks Harry
    noteG = 196
    noteB = 247
    noteC = 261
    noteD = 293
    noteE = 330
    #  brick.sound.beep(frequency=500, duration=100, volume=30)
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
    #  last four notes
    wait(100)
    brick.sound.beep(noteD, 440, 75)
    brick.sound.beep(noteC, 440, 75)
    brick.sound.beep(noteB, 220, 80)
    brick.sound.beep(noteG, 220, 85)

    brick.light(None)

def forward(stopdist):
    robot.drive(-100, 0)
    stopdist = int(stopdist)
    while ForwardSensor.distance() > stopdist:
        wait(1)
    robot.stop()
    
def backward(time):
    robot.drive(100, 0)     
    wait(time)

def rightturn():
    left.run(-50, 1200)

def leftturn():
    left.run(50, 1200)

def main



forward(200)
foundvictim()
#  brick.sound.beep()
#  MA.backward(2000)
#  brick.sound.beep()
rightturn()
#  brick.sound.beep()
leftturn()
#  brick.sound.beep()
#  colourchecker()
'''
TODO
• GET COLOUR SENSOR!!!!!!!!!!!!!!!
• We must make a function that tells it to scan along the left-hand
side of the maze
• We must check out how to use our sensors and finalise sensor position
• Then, we use it to write a function to identify victims
AND to go there and beep.
• write function to give resources to identified victims

Finally, we can write function to make it more likely for robot to exit
at the entry position and earn bonus points there.
'''

