import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class CheckableComboBox(QComboBox):
	def __init__(self):
		super().__init__()
		self._changed = False

		self.view().pressed.connect(self.handleItemPressed)

	def setItemChecked(self, index, checked=False):
		item = self.model().item(index, self.modelColumn()) # QStandardItem object

		if checked:
			item.setCheckState(Qt.Checked)
		else:
			item.setCheckState(Qt.Unchecked)

	def handleItemPressed(self, index):
		item = self.model().itemFromIndex(index)

		if item.checkState() == Qt.Checked:
			item.setCheckState(Qt.Unchecked)
		else:
			item.setCheckState(Qt.Checked)
		self._changed = True


	def hidePopup(self):
		if not self._changed:
			super().hidePopup()
		self._changed = False

	def itemChecked(self, index):
		item = self.model().item(index, self.modelColumn())
		return item.checkState() == Qt.Checked

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(500, 150)

		mainLayout = QVBoxLayout()

		self.combo = CheckableComboBox()
		mainLayout.addWidget(self.combo)

		for i in range(6):
			self.combo.addItem('Item {0}'.format(str(i)))
			self.combo.setItemChecked(i, False)
		
		btn = QPushButton('Print Values')
		btn.clicked.connect(self.getValue)
		mainLayout.addWidget(btn)

		self.setLayout(mainLayout)

	def getValue(self):
		for i in range(self.combo.count()):
			print('Index: {0} is checked {1}'.format(i, self.combo.itemChecked(i)))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet('''
		QWidget {
			font-size: 16px;
		}
	''')

	myApp = MyApp()
	myApp.show()

	app.exit(app.exec_())	