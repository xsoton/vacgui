import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
	QApplication, QMainWindow, QWidget,
	QVBoxLayout, QHBoxLayout, QSplitter, QTextEdit)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle("My App")

		self.vlayout = QVBoxLayout()
		# self.hlayout = QHBoxLayout()

		self.vsplitter = QSplitter(Qt.Orientation.Vertical)
		self.hsplitter = QSplitter(Qt.Orientation.Horizontal)

		# self.hwidget = QWidget()
		self.b1 = QTextEdit("1")
		self.b2 = QTextEdit("2")
		self.b3 = QTextEdit("3")
		self.b4 = QTextEdit("4")

		self.hsplitter.addWidget(self.b1)
		self.hsplitter.addWidget(self.b2)

		self.vsplitter.addWidget(self.hsplitter)
		self.vsplitter.addWidget(self.b3)
		self.vsplitter.addWidget(self.b4)

		self.vlayout.addWidget(self.vsplitter)

		# self.vlayout.addWidget(self.hwidget)
		# self.vlayout.addWidget(self.hsplitter)
		# self.vlayout.addWidget(self.b3)

		self.mainwidget = QWidget()
		self.mainwidget.setLayout(self.vlayout)

		self.setCentralWidget(self.vsplitter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
