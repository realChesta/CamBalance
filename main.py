import serial
from random import randint
import tracking

arduino = serial.Serial("\\\\.\\COM3")
print(arduino.readline())
print(arduino.writeTimeout)


def onPosition(pos):
    deg = int(pos[0] / 1.6)
    print(deg)
    arduino.write((str(deg) + '\r').encode('UTF-8'))
    print(arduino.readline())

#tracking.track(onPosition)

while True:
    #deg = (str(randint(1, 359)) + "\n").encode('UTF-8')
    deg = (input("Enter desired degrees: ") + "\n").encode('UTF-8')
    print(deg)
    arduino.write(deg)
    print(arduino.readline())

