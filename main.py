import serial
from random import randint
import tracking


# arduino = serial.Serial("\\\\.\\COM3")
# print(arduino.readline())
# print(arduino.writeTimeout)

def onNewPos(pos, history):
    print(pos)

tracking.track(onNewPos)

# while True:
#     deg = (str(randint(1, 359)) + "\n").encode('UTF-8')
#     #(input("Enter desired degrees: ") + "\n").encode('UTF-8')
#     print(deg)
#     arduino.write(deg)
#     print(arduino.readline())

