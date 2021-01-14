import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Demo(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Center the app')
		self.center()
		self.show()
		
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	sys.exit(app.exec_())