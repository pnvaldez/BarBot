from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import sys
import serial
import time
import csv

from find_arduino_port import get_ports, find_arduino
from barbot_classes import *
from barbot_ui import *

flowrate = 1.31 #ml/sec

found_ports = get_ports()        
arduino_port = find_arduino(found_ports)

if arduino_port != 'None':
    ser = serial.Serial(arduino_port, baudrate = 9600, timeout=1)
    print('Connected to ' + arduino_port)

else:
    print('Connection Issue!')

time.sleep(3)
ser.write(bytes(str(flowrate), 'utf-8'))


#Run the Program
barbot_utility = Utility(ser)
app=QApplication(sys.argv)
ex=Window(barbot_utility)
sys.exit(app.exec_())