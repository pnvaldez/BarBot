from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import RPi.GPIO as GPIO
import sys
import time


from barbot_classes import *
from barbot_ui import *

#GPIO Setup
GPIO.setmode(GPIO.BCM)

pump_1 = 26
pump_2 = 19
pump_3 = 13
pump_4 = 6

GPIO.setup(pump_1, GPIO.OUT)
GPIO.setup(pump_2, GPIO.OUT)
GPIO.setup(pump_3, GPIO.OUT)
GPIO.setup(pump_4, GPIO.OUT)

GPIO.output(pump_1, 1)
GPIO.output(pump_2, 1)
GPIO.output(pump_3, 1)
GPIO.output(pump_4, 1)

#Run the Program
barbot_utility = Utility()
app=QApplication(sys.argv)
ex=Window(barbot_utility)
sys.exit(app.exec_())