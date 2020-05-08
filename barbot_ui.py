from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

import sys
from barbot_classes import *


main_button_style = """
	QWidget {
		background-color: rgb(29,30,58);
		color: rgb(220,220,220);
		border-width: 3px;
		border-radius: 10px;
		border-color: rgb(29, 30, 58);
		padding: 4px;
		}
	"""
ghost_button_style = main_button_style

back_button_style = """
	QWidget {
		background-color: rgb(216, 216, 216);
		border-radius: 7px;
		}
	"""
label_style = """
	QWidget {
		background-color: rgb(216, 216, 216);
		color: rgb(29,30,58);
		}
	"""

background_style = "background-color: rgb(240,240,240);"

logo_font = QtGui.QFont()
logo_font.setFamily("Myanmar Text")
logo_font.setPointSize(16)
logo_font.setBold(True)
logo_font.setWeight(75)

logo_style_1 = "color: rgb(255,78,96);"
logo_style_2 = "color: rgb(69, 226, 228)"

drink_logo = "Images/drink_icon.png"
arrow_icon = "Images/back_arrow.png"


######GUI
class Window(QMainWindow):
	def __init__(self,loadout):
		super().__init__()
		self.title = "first_screen"
		self.top = 0
		self.left = 0
		self.height = 240
		self.width = 320
		self.loadout = loadout
		self.InitUi()

	def InitUi(self):
		MainWindow = QtWidgets.QMainWindow()
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setStyleSheet(background_style)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(20)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)

		drink_button = QtWidgets.QPushButton('Drink', self)
		drink_button.setGeometry(QtCore.QRect(10, 10, 301, 61))
		drink_button.setFont(font)
		drink_button.setStyleSheet(main_button_style)

		drink_button.clicked.connect(self.drink_clicked)

		setup_button = QtWidgets.QPushButton('Setup', self)
		setup_button.setGeometry(QtCore.QRect(10, 80, 301, 61))
		setup_button.setFont(font)
		setup_button.setStyleSheet(main_button_style)
		setup_button.clicked.connect(self.setup_clicked)

		logo_txt1 =QtWidgets.QLabel("Bar", self)
		logo_txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt1.setGeometry(QtCore.QRect(210, 160, 41, 31))
		logo_txt1.setFont(logo_font)
		logo_txt1.setStyleSheet("color: rgb(255,78,96);")

		logo_txt2 =QtWidgets.QLabel("Bot", self)
		logo_txt2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt2.setGeometry(QtCore.QRect(245, 160, 41, 31))
		logo_txt2.setFont(logo_font)
		logo_txt2.setStyleSheet("color: rgb(69,226,228);")

		logo_pic = QtWidgets.QLabel(self)
		logo_pic.setGeometry(QtCore.QRect(280,160,31,31))
		logo_pic.setPixmap(QtGui.QPixmap(drink_logo))
		logo_pic.setScaledContents(True)
		self.show()

	@pyqtSlot()
	def drink_clicked(self):
		self.cams = drink_window(self.loadout)
		self.cams.show()
		self.close()

	@pyqtSlot()
	def setup_clicked(self):
		self.cams = setup_window(self.loadout)
		self.cams.show()
		self.close()

class drink_window(QMainWindow):
	def __init__(self, loadout):
		super().__init__()
		self.title = "first_screen"
		self.top = 0
		self.left = 0
		self.height = 240
		self.width = 320
		self.loadout = loadout
		self.InitUi()

	def InitUi(self):
		MainWindow = QtWidgets.QMainWindow()
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setStyleSheet(background_style)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(arrow_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setPointSize(20)

		recipe_button = QtWidgets.QPushButton('Recipe List', self)
		recipe_button.setGeometry(QtCore.QRect(10, 10, 301, 61))
		recipe_button.setFont(font)
		recipe_button.setStyleSheet(main_button_style)
		recipe_button.clicked.connect(self.recipe_clicked)

		custom_button = QtWidgets.QPushButton('+ Custom', self)
		custom_button.setGeometry(QtCore.QRect(10, 80, 301, 61))
		custom_button.setFont(font)
		custom_button.setStyleSheet(main_button_style)
		custom_button.clicked.connect(self.custom_clicked)

		font.setPointSize(8)

		back_button = QtWidgets.QToolButton(self)
		back_button.setGeometry(QtCore.QRect(0, 160, 161, 31))
		back_button.setFont(font)
		back_button.setIcon(icon)
		back_button.setStyleSheet(back_button_style)
		back_button.clicked.connect(self.back_clicked)

		logo_txt1 =QtWidgets.QLabel("Bar", self)
		logo_txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt1.setGeometry(QtCore.QRect(210, 160, 41, 31))
		logo_txt1.setFont(logo_font)
		logo_txt1.setStyleSheet("color: rgb(255,78,96);")

		logo_txt2 =QtWidgets.QLabel("Bot", self)
		logo_txt2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt2.setGeometry(QtCore.QRect(245, 160, 41, 31))
		logo_txt2.setFont(logo_font)
		logo_txt2.setStyleSheet("color: rgb(69,226,228);")

		logo_pic = QtWidgets.QLabel(self)
		logo_pic.setGeometry(QtCore.QRect(280,160,31,31))
		logo_pic.setPixmap(QtGui.QPixmap(drink_logo))
		logo_pic.setScaledContents(True)

		#self.ounce_label = QtWidgets.QLabel('0 oz', self)
		#self.ounce_label.setAlignment(Qt.AlignCenter)
		#self.ounce_label.setGeometry(QtCore.QRect(100, 130, 121, 51))
		#self.ounce_label.setFont(font)
		#self.ounce_label.setStyleSheet(label_style)


	@pyqtSlot()
	def recipe_clicked(self):
		self.cams = recipe_window(self.loadout)
		self.cams.show()
		self.close()

	@pyqtSlot()
	def custom_clicked(self):
		self.cams = custom_window(self.loadout)
		self.cams.show()
		self.close()

	@pyqtSlot()
	def back_clicked(self):
		self.cams = Window(self.loadout)
		self.cams.show()
		self.close()

class recipe_window(QMainWindow):
	def __init__(self, loadout):
		super().__init__()
		self.title = "first_screen"
		self.top = 0
		self.left = 0
		self.height = 240
		self.width = 320
		self.loadout = loadout
		self.drink_list = loadout.get_makeable_drinks()
		self.indx = 0
		self.list_len = len(self.drink_list) - 1
		self.InitUi()

	def InitUi(self):
		MainWindow = QtWidgets.QMainWindow()
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setStyleSheet(background_style)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(arrow_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setPointSize(20)

		self.recipe_button = QtWidgets.QPushButton(self.drink_list[0][0], self)
		self.recipe_button.setGeometry(QtCore.QRect(10, 10, 301, 61))
		self.recipe_button.setFont(font)
		self.recipe_button.setStyleSheet(main_button_style)

		self.recipe_button.clicked.connect(self.recipe_clicked)

		font.setPointSize(16)
		previous_button = QtWidgets.QPushButton('Previous', self)
		previous_button.setGeometry(QtCore.QRect(10, 80, 141, 61))
		previous_button.setFont(font)
		previous_button.setStyleSheet(ghost_button_style)

		previous_button.clicked.connect(self.previous_clicked)

		next_button = QtWidgets.QPushButton('Next', self)
		next_button.setGeometry(QtCore.QRect(170, 80, 141, 61))
		next_button.setFont(font)
		next_button.setStyleSheet(ghost_button_style)
		next_button.clicked.connect(self.next_clicked)

		back_button = QtWidgets.QToolButton(self)
		back_button.setGeometry(QtCore.QRect(0, 160, 161, 31))
		back_button.setFont(font)
		back_button.setIcon(icon)
		back_button.setStyleSheet(back_button_style)
		back_button.clicked.connect(self.back_clicked)

		logo_txt1 =QtWidgets.QLabel("Bar", self)
		logo_txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt1.setGeometry(QtCore.QRect(210, 160, 41, 31))
		logo_txt1.setFont(logo_font)
		logo_txt1.setStyleSheet("color: rgb(255,78,96);")

		logo_txt2 =QtWidgets.QLabel("Bot", self)
		logo_txt2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt2.setGeometry(QtCore.QRect(245, 160, 41, 31))
		logo_txt2.setFont(logo_font)
		logo_txt2.setStyleSheet("color: rgb(69,226,228);")

		logo_pic = QtWidgets.QLabel(self)
		logo_pic.setGeometry(QtCore.QRect(280,160,31,31))
		logo_pic.setPixmap(QtGui.QPixmap(drink_logo))
		logo_pic.setScaledContents(True)

	@pyqtSlot()
	def recipe_clicked(self):
		#self.cams = recipe_window(self.loadout)
		#self.cams.show()
		#self.close()
		curr_drink = Drink(self.drink_list[self.indx], self.loadout.get_loadout(), self.loadout.ser)
		self.recipe_button.setText("Pouring ...")
		curr_drink.make_drink()
		time.sleep(3)
		self.recipe_button.setText(self.drink_list[self.indx][0])

	@pyqtSlot()
	def previous_clicked(self):
		self.indx -= 1
		if self.indx < 0:
			self.indx = self.list_len
		self.recipe_button.setText(self.drink_list[self.indx][0])


	@pyqtSlot()
	def next_clicked(self):
		self.indx += 1
		if self.indx > self.list_len:
			self.indx = 0
		self.recipe_button.setText(self.drink_list[self.indx][0])

	@pyqtSlot()
	def back_clicked(self):
		self.cams = drink_window(self.loadout)
		self.cams.show()
		self.close()

class custom_window(QMainWindow):
	def __init__(self, loadout):
		super().__init__()
		self.title = "first_screen"
		self.top = 0
		self.left = 0
		self.height = 240
		self.width = 320
		self.loadout = loadout
		self.indx = 0
		self.InitUi()

	def InitUi(self):
		MainWindow = QtWidgets.QMainWindow()
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setStyleSheet(background_style)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.curr_loadout = self.loadout.get_loadout()
		self.curr_recipe = ["Custom Drink",{}]
		self.indx = 0
		self.ounces = 0
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(arrow_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setPointSize(20)

		self.recipe_button = QtWidgets.QPushButton("Add: " + self.curr_loadout[0], self)
		self.recipe_button.setGeometry(QtCore.QRect(10, 10, 301, 61))
		self.recipe_button.setFont(font)
		self.recipe_button.setStyleSheet(main_button_style)
		self.recipe_button.clicked.connect(self.recipe_clicked)

		font.setPointSize(16)
		minus_button = QtWidgets.QPushButton('- 0.5', self)
		minus_button.setGeometry(QtCore.QRect(10, 80, 81, 61))
		minus_button.setFont(font)
		minus_button.setStyleSheet(ghost_button_style)
		minus_button.clicked.connect(self.minus_clicked)

		add_button = QtWidgets.QPushButton('+ 0.5', self)
		add_button.setGeometry(QtCore.QRect(230, 80, 81, 61))
		add_button.setFont(font)
		add_button.setStyleSheet(ghost_button_style)
		add_button.clicked.connect(self.add_clicked)

		self.ounce_label = QtWidgets.QLabel('0 oz', self)
		self.ounce_label.setAlignment(Qt.AlignCenter)
		self.ounce_label.setGeometry(QtCore.QRect(80, 80, 161, 61))
		self.ounce_label.setFont(font)
		self.ounce_label.setStyleSheet(label_style)

		back_button = QtWidgets.QToolButton(self)
		back_button.setGeometry(QtCore.QRect(0, 160, 161, 31))
		back_button.setFont(font)
		back_button.setIcon(icon)
		back_button.setStyleSheet(back_button_style)
		back_button.clicked.connect(self.back_clicked)

		logo_txt1 =QtWidgets.QLabel("Bar", self)
		logo_txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt1.setGeometry(QtCore.QRect(210, 160, 41, 31))
		logo_txt1.setFont(logo_font)
		logo_txt1.setStyleSheet("color: rgb(255,78,96);")

		logo_txt2 =QtWidgets.QLabel("Bot", self)
		logo_txt2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt2.setGeometry(QtCore.QRect(245, 160, 41, 31))
		logo_txt2.setFont(logo_font)
		logo_txt2.setStyleSheet("color: rgb(69,226,228);")

		logo_pic = QtWidgets.QLabel(self)
		logo_pic.setGeometry(QtCore.QRect(280,160,31,31))
		logo_pic.setPixmap(QtGui.QPixmap(drink_logo))
		logo_pic.setScaledContents(True)


	@pyqtSlot()
	def recipe_clicked(self):
		if self.ounces > 0:
			key = self.curr_loadout[self.indx]
			self.curr_recipe[1][key] = self.ounces

		if self.indx < len(self.curr_loadout) - 1:
			self.ounces = 0
			self.indx += 1
			self.recipe_button.setText("Add: " + self.curr_loadout[self.indx])
			self.ounce_label.setText(str(self.ounces) + " oz")
			print(self.curr_recipe)

		else:

			print(self.curr_recipe)
			print(self.curr_loadout)
			curr_drink = Drink(self.curr_recipe, self.curr_loadout, self.loadout.ser)
			curr_drink.make_drink()
			self.cams = drink_window(self.loadout)
			self.cams.show()
			self.close()

	@pyqtSlot()
	def minus_clicked(self):
		if self.ounces > 0:
			self.ounces -= 0.5
		self.ounce_label.setText(str(self.ounces) + " oz")


	@pyqtSlot()
	def add_clicked(self):
		if self.ounces < 10:
			self.ounces += 0.5
		self.ounce_label.setText(str(self.ounces) + " oz")
		

	@pyqtSlot()
	def back_clicked(self):
		if self.indx == 0:
			self.cams = drink_window(self.loadout)
			self.cams.show()
			self.close()
		else:
			self.indx -= 1
			curr_key = self.curr_loadout[self.indx]
			for key in self.curr_recipe[1]:
				if curr_key == key:
					del self.curr_recipe[1][curr_key]
					break
			self.recipe_button.setText("Add: " + self.curr_loadout[self.indx])

class setup_window(QMainWindow):
	def __init__(self, loadout):
		super().__init__()
		self.title = "first_screen"
		self.top = 0
		self.left = 0
		self.height = 240
		self.width = 320
		self.loadout = loadout
		self.InitUi()

	def InitUi(self):
		MainWindow = QtWidgets.QMainWindow()
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setStyleSheet(background_style)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(arrow_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setPointSize(20)

		loadout_button = QtWidgets.QPushButton('Change Loadout', self)
		loadout_button.setGeometry(QtCore.QRect(10, 10, 301, 61))
		loadout_button.setFont(font)
		loadout_button.setStyleSheet(main_button_style)
		loadout_button.clicked.connect(self.loadout_clicked)

		prime_flush_button = QtWidgets.QPushButton('Prime/Flush', self)
		prime_flush_button.setGeometry(QtCore.QRect(10, 80, 301, 61))
		prime_flush_button.setFont(font)
		prime_flush_button.setStyleSheet(main_button_style)
		prime_flush_button.clicked.connect(self.prime_flush_clicked)

		back_button = QtWidgets.QToolButton(self)
		back_button.setGeometry(QtCore.QRect(0, 160, 161, 31))
		back_button.setFont(font)
		back_button.setIcon(icon)
		back_button.setStyleSheet(back_button_style)
		back_button.clicked.connect(self.back_clicked)

		logo_txt1 =QtWidgets.QLabel("Bar", self)
		logo_txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt1.setGeometry(QtCore.QRect(210, 160, 41, 31))
		logo_txt1.setFont(logo_font)
		logo_txt1.setStyleSheet("color: rgb(255,78,96);")

		logo_txt2 =QtWidgets.QLabel("Bot", self)
		logo_txt2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt2.setGeometry(QtCore.QRect(245, 160, 41, 31))
		logo_txt2.setFont(logo_font)
		logo_txt2.setStyleSheet("color: rgb(69,226,228);")

		logo_pic = QtWidgets.QLabel(self)
		logo_pic.setGeometry(QtCore.QRect(280,160,31,31))
		logo_pic.setPixmap(QtGui.QPixmap(drink_logo))
		logo_pic.setScaledContents(True)

	@pyqtSlot()
	def loadout_clicked(self):
		self.cams = loadout_window(self.loadout)
		self.cams.show()
		self.close()

	@pyqtSlot()
	def prime_flush_clicked(self):
		self.cams = prime_flush_window(self.loadout)
		self.cams.show()
		self.close()

	@pyqtSlot()
	def back_clicked(self):
		self.cams = Window(self.loadout)
		self.cams.show()
		self.close()

class prime_flush_window(QMainWindow):
	def __init__(self, loadout):
		super().__init__()
		self.title = "first_screen"
		self.top = 0
		self.left = 0
		self.height = 240
		self.width = 320
		self.loadout = loadout
		self.InitUi()

	def InitUi(self):
		MainWindow = QtWidgets.QMainWindow()
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setStyleSheet(background_style)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(arrow_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setPointSize(20)

		prime_button = QtWidgets.QPushButton('Prime Pumps', self)
		prime_button.setGeometry(QtCore.QRect(10, 10, 301, 61))
		prime_button.setFont(font)
		prime_button.setStyleSheet(main_button_style)
		prime_button.clicked.connect(self.prime_clicked)

		flush_button = QtWidgets.QPushButton('Flush Pumps', self)
		flush_button.setGeometry(QtCore.QRect(10, 80, 301, 61))
		flush_button.setFont(font)
		flush_button.setStyleSheet(main_button_style)
		flush_button.clicked.connect(self.flush_clicked)

		back_button = QtWidgets.QToolButton(self)
		back_button.setGeometry(QtCore.QRect(0, 160, 161, 31))
		back_button.setFont(font)
		back_button.setIcon(icon)
		back_button.setStyleSheet(back_button_style)
		back_button.clicked.connect(self.back_clicked)

		logo_txt1 =QtWidgets.QLabel("Bar", self)
		logo_txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt1.setGeometry(QtCore.QRect(210, 160, 41, 31))
		logo_txt1.setFont(logo_font)
		logo_txt1.setStyleSheet("color: rgb(255,78,96);")

		logo_txt2 =QtWidgets.QLabel("Bot", self)
		logo_txt2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt2.setGeometry(QtCore.QRect(245, 160, 41, 31))
		logo_txt2.setFont(logo_font)
		logo_txt2.setStyleSheet("color: rgb(69,226,228);")

		logo_pic = QtWidgets.QLabel(self)
		logo_pic.setGeometry(QtCore.QRect(280,160,31,31))
		logo_pic.setPixmap(QtGui.QPixmap(drink_logo))
		logo_pic.setScaledContents(True)

	@pyqtSlot()
	def prime_clicked(self):
		self.loadout.prime_pumps()

	@pyqtSlot()
	def flush_clicked(self):
		self.loadout.flush_pumps()
		
	@pyqtSlot()
	def back_clicked(self):
		self.cams = setup_window(self.loadout)
		self.cams.show()
		self.close()

class loadout_window(QMainWindow):
	def __init__(self, loadout):
		super().__init__()
		self.title = "first_screen"
		self.top = 0
		self.left = 0
		self.height = 240
		self.width = 320
		self.loadout = loadout
		self.indx = 0
		self.pump = 1
		self.ingredients = self.loadout.get_ingredients()
		self.ingredient_len = len(self.ingredients) - 1
		self.InitUi()

	def InitUi(self):
		MainWindow = QtWidgets.QMainWindow()
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		self.setStyleSheet(background_style)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.curr_loadout = []
		self.indx = 0
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(arrow_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		font.setPointSize(20)

		self.loadout_button = QtWidgets.QPushButton("Add Pump " + str(self.pump), self)
		self.loadout_button.setGeometry(QtCore.QRect(10, 10, 301, 61))
		self.loadout_button.setFont(font)
		self.loadout_button.setStyleSheet(main_button_style)
		self.loadout_button.clicked.connect(self.loadout_clicked)

		font.setPointSize(11)
		previous_button = QtWidgets.QPushButton('Previous', self)
		previous_button.setGeometry(QtCore.QRect(10, 80, 81, 61))
		previous_button.setFont(font)
		previous_button.setStyleSheet(ghost_button_style)
		previous_button.clicked.connect(self.previous_clicked)

		next_button = QtWidgets.QPushButton('Next', self)
		next_button.setGeometry(QtCore.QRect(230, 80, 81, 61))
		next_button.setFont(font)
		next_button.setStyleSheet(ghost_button_style)
		next_button.clicked.connect(self.next_clicked)

		self.ingredient_label = QtWidgets.QLabel(self.ingredients[0], self)
		self.ingredient_label.setAlignment(Qt.AlignCenter)
		self.ingredient_label.setGeometry(QtCore.QRect(80, 80, 161, 61))
		self.ingredient_label.setFont(font)
		self.ingredient_label.setStyleSheet(label_style)

		back_button = QtWidgets.QToolButton(self)
		back_button.setGeometry(QtCore.QRect(0, 160, 161, 31))
		back_button.setFont(font)
		back_button.setIcon(icon)
		back_button.setStyleSheet(back_button_style)
		back_button.clicked.connect(self.back_clicked)

		logo_txt1 =QtWidgets.QLabel("Bar", self)
		logo_txt1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt1.setGeometry(QtCore.QRect(210, 160, 41, 31))
		logo_txt1.setFont(logo_font)
		logo_txt1.setStyleSheet("color: rgb(255,78,96);")

		logo_txt2 =QtWidgets.QLabel("Bot", self)
		logo_txt2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		logo_txt2.setGeometry(QtCore.QRect(245, 160, 41, 31))
		logo_txt2.setFont(logo_font)
		logo_txt2.setStyleSheet("color: rgb(69,226,228);")

		logo_pic = QtWidgets.QLabel(self)
		logo_pic.setGeometry(QtCore.QRect(280,160,31,31))
		logo_pic.setPixmap(QtGui.QPixmap(drink_logo))
		logo_pic.setScaledContents(True)

	@pyqtSlot()
	def loadout_clicked(self):
		if self.ingredients[self.indx] == "None":
			self.curr_loadout.append("")
		else:
			self.curr_loadout.append(self.ingredients[self.indx])

		if self.pump == 4:
			self.loadout.change_loadout(self.curr_loadout)
			print(self.loadout.get_loadout())
			self.cams = setup_window(self.loadout)
			self.cams.show()
			self.close()

		self.pump += 1
		self.loadout_button.setText("Add Pump " + str(self.pump))

		print(self.curr_loadout)
		

	@pyqtSlot()
	def previous_clicked(self):
		if self.indx == 0:
			self.indx = self.ingredient_len
		else:
			self.indx -= 1
		self.ingredient_label.setText(self.ingredients[self.indx])


	@pyqtSlot()
	def next_clicked(self):
		if self.indx == self.ingredient_len:
			self.indx = 0
		else:
			self.indx += 1
		self.ingredient_label.setText(self.ingredients[self.indx])
		

	@pyqtSlot()
	def back_clicked(self):
		if self.pump == 1:
			self.cams = setup_window(self.loadout)
			self.cams.show()
			self.close()
		else:
			self.pump -= 1
			self.curr_loadout = self.curr_loadout[:-1]
			self.loadout_button.setText("Add Pump " + str(self.pump))
