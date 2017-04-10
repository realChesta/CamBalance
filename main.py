import serial
from tracking import Tracking


class CamBalance:
    lastStep = 0
    tracking = Tracking()

    def sendStep(self, step):
        if step is not self.lastStep:
            print(step)
            self.arduino.write((str(step) + "\n").encode('UTF-8'))
            print(self.arduino.readline())
            self.lastStep = step

    def onNewPos(self, pos, history):
        print(pos)

    def start(self, port="\\\\.\\COM3"):
        self.arduino = serial.Serial(port)
        print(self.arduino.readline())
        self.tracking.start(self.onNewPos)


balance = CamBalance()
balance.start()
