import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer


class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.n = 10

		layout = QVBoxLayout()
		self.setLayout(layout)

		for i in range(self.n):
			btn = QPushButton()
			btn.setText(str(i))
			btn.setObjectName('Button {0}'.format(i))
			layout.addWidget(btn)

		timer = QTimer(self)
		timer.setInterval(1000)
		timer.timeout.connect(self.updateText)
		timer.start()

	def updateText(self):
		for i in range(self.n):
			child = self.findChild(QPushButton, 'Button {0}'.format(i))
			counter = int(child.text())
			child.setText(str(counter + 1))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet('''
		QWidget {
			font-size: 35px;
		}
	''')
	
	myApp = MyApp()
	myApp.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')