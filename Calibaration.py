from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import MotorActions as MA
cSensor = ColorSensor(Port.S2)

def colourchecker():
    #Working now
    while True:
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