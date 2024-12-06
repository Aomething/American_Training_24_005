import time
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class testWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.testPix = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.pnggrayStar.png")
		self.testPix2 = self.testPix.scaled(150, 150)
		self.testImage = QLabel()
		self.testImage.setPixmap(self.testPix2)
		self.testImage.setParent(self)
		self.testImage.setFixedSize(150,150)
		self.testImage.move(0,0)

class testWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.testWid = testWidget()
		self.testWid.show()
		self.testWid.setFixedSize(800,450)

if __name__ == "__main__":
	app = QApplication([])
	window = testWindow()
	sys.exit(app.exec())
