import sys		
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QTimer


class AppDemo(QPushButton):
	def __init__(self):
		super().__init__('My Button')
		self.resize(400, 400)
		self.setStyleSheet('font-size: 40px;')
		self.flag = True

		timer = QTimer(self, interval=1000)
		timer.timeout.connect(self.flashing)
		timer.start()

		self.clicked.connect(lambda: print('hello world'))

	def flashing(self):
		if self.flag:
			self.setStyleSheet('background-color: none; font-size: 40px')
		else:
			self.setStyleSheet('background-color: orange; font-size: 40px')

		self.flag = not self.flag


if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = AppDemo()
	demo.show()
	
	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')