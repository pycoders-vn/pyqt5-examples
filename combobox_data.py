import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout


class AppDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.setStyleSheet('font-size: 30px;')
		self.setWindowTitle('Dependent ComboBox Dropdown')
		self.setMinimumWidth(600)

		layout = QHBoxLayout()
		self.setLayout(layout)

		self.comboState = QComboBox()
		self.comboState.addItem('CA', ['San Francisco', 'Oakland', 'San Jose']) # index 0
		self.comboState.addItem('IL', ['Chicago', 'Springfield', 'Evanston', 'Skokie', 'Lincolnwood']) # index 1
		layout.addWidget(self.comboState)
			
		self.comboCity = QComboBox()
		layout.addWidget(self.comboCity)

		self.comboState.currentIndexChanged.connect(self.updateCityCombo)

		self.updateCityCombo(self.comboState.currentIndex())

	def updateCityCombo(self, index):
		self.comboCity.clear()
		cities = self.comboState.itemData(index)
		if cities:
			self.comboCity.addItems(cities)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = AppDemo()
	demo.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')