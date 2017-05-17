import serial
from math import ceil
from tracking import Tracking


class CamBalance:
    lastStep = 0
    tracking = Tracking()

    def sendStep(self, step):
        if step != self.lastStep:
            print(step)
            self.arduino.write((str(step) + "\n").encode('UTF-8'))
            print(self.arduino.readline())
            self.lastStep = step

    def sendAngle(self, angle):
        self.sendStep(ceil(angle / 7.5))

    def onNewPos(self, pos, history):
        self.sendAngle(pos[0] / 16)

    def start(self, port="\\\\.\\COM3"):
        self.arduino = serial.Serial(port)
        print(self.arduino.readline())
        self.tracking.start(self.onNewPos)
        self.sendStep(12) #set angle to neutral pos


balance = CamBalance()
balance.start()
