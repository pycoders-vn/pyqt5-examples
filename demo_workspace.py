import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMdiArea, QCalendarWidget, QTextEdit, QPushButton)

class AppDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(800, 800)

		workspace = QMdiArea(self)
		workspace.resize(self.rect().width(), self.rect().height())

		self.calendar = QCalendarWidget()
		self.calendar.clicked.connect(lambda date: print(date.getDate()))
		workspace.addSubWindow(self.calendar)

		self.button = QPushButton('My Button')
		self.button.clicked.connect(lambda: print('button is clicked'))
		workspace.addSubWindow(self.button)

		textEditor = QTextEdit()
		workspace.addSubWindow(textEditor)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

	sys.exit(app.exec_())