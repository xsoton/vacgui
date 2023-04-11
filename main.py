import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor

class GraphWidget(QWidget):
	def __init__(self):
		super(GraphWidget, self).__init__()
		self.b1 = QTextEdit("1")
		self.lauout = QVBoxLayout()
		self.lauout.addWidget(self.b1)
		self.setLayout(self.lauout)

class ParametersWidget(QWidget):
	def __init__(self):
		super(ParametersWidget, self).__init__()

		# === action ===

		self.newButton = QPushButton("New")
		self.nextButton = QPushButton("Next")
		self.startButton = QPushButton("Start")

		actionButtonLayout = QHBoxLayout()
		actionButtonLayout.addWidget(self.newButton)
		actionButtonLayout.addWidget(self.nextButton)
		actionButtonLayout.addWidget(self.startButton)

		actionButtons = QWidget()
		actionButtons.setLayout(actionButtonLayout)

		# === head ===
		label00 = QLabel("Sample:")
		self.label02 = QLabel("SAMPLE")
		label10 = QLabel("Comment:")
		self.label12 = QLabel("COMMENT")
		label20 = QLabel("Date:")
		self.label22 = QLabel("DATETIME")
		label30 = QLabel("Status:")
		self.label32 = QLabel("STATUS")

		headLayout = QGridLayout()
		headLayout.addWidget(label00, 0, 0)
		headLayout.addWidget(self.label02, 0, 2)
		headLayout.addWidget(label10, 1, 0)
		headLayout.addWidget(self.label12, 1, 2)
		headLayout.addWidget(label20, 2, 0)
		headLayout.addWidget(self.label22, 2, 2)
		headLayout.addWidget(label30, 3, 0)
		headLayout.addWidget(self.label32, 3, 2)

		head = QWidget()
		head.setLayout(headLayout)

		# === list ===

		self.plist = QListWidget()

		self.addButton = QPushButton("Add")
		self.delButton = QPushButton("Del")
		self.editButton = QPushButton("Edit")

		listButtonLayout = QHBoxLayout()
		listButtonLayout.addWidget(self.addButton)
		listButtonLayout.addWidget(self.delButton)
		listButtonLayout.addWidget(self.editButton)

		listButtons = QWidget()
		listButtons.setLayout(listButtonLayout)

		# === all together ===

		lauout = QVBoxLayout()
		lauout.addWidget(actionButtons)
		lauout.addWidget(head)
		lauout.addWidget(self.plist)
		lauout.addWidget(listButtons)
		self.setLayout(lauout)

class FilesWidget(QWidget):
	def __init__(self):
		super(FilesWidget, self).__init__()
		self.b3 = QListWidget()
		self.lauout = QVBoxLayout()
		self.lauout.addWidget(self.b3)
		self.setLayout(self.lauout)

class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle("vac")

		self.vsplitter = QSplitter(Qt.Orientation.Vertical)
		self.hsplitter = QSplitter(Qt.Orientation.Horizontal)

		self.graph = GraphWidget()
		self.parameters = ParametersWidget()
		self.files = FilesWidget()

		self.hsplitter.addWidget(self.graph)
		self.hsplitter.addWidget(self.parameters)

		self.vsplitter.addWidget(self.hsplitter)
		self.vsplitter.addWidget(self.files)

		self.setCentralWidget(self.vsplitter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
