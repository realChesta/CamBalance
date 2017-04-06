import serial
from random import randint

arduino = serial.Serial("\\\\.\\COM3")
print(arduino.readline())
print(arduino.writeTimeout)

while True:
    deg = (str(randint(1, 359)) + "\n").encode('UTF-8')
    #(input("Enter desired degrees: ") + "\n").encode('UTF-8')
    print(deg)
    arduino.write(deg)
    print(arduino.readline())

