import sys
import pkgutil as pkg
# pip install PyQt5 to install the library
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QListWidget, QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QStringListModel, QFile, QTextStream, Qt
from PyQt5.QtGui import QIcon

import PyQt5.QtWidgets
import PyQt5.QtSql
import PyQt5.QtMultimedia
import PyQt5.QtWebEngineWidgets
import PyQt5.QtWebEngine
import PyQt5.QtWebEngineCore
import PyQt5.QtPositioning
import PyQt5.QtNetwork


# Based on your imported modules

class HelperText(QTextEdit):
	def __init__(self, obj):
		super().__init__()
		self.setStyleSheet('''
			background-color: white;
			color: black;
			font-size: 35px;
		''')

		self.resize(1200, 1000)
		self.setWindowTitle('Help Information')
		self.setReadOnly(True)

		help_text = obj.__doc__
		self.setText(help_text)


class PythonNavigator(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(1600, 1200)
		self.setWindowTitle('Qt Module Navigation')
		self.setWindowIcon(self.style().standardIcon(0))
		self.module_object = None
		self.model = None

		self.layout = QVBoxLayout()

		available_modules = ('QtWidgets', 'QtCore', 'QtGui', 'QtSql', 'QtNetwork', 'QtPositioning', 'QtWebEngine', 'QtWebEngineCore', 'QtWebEngineWidgets')

		# combobox widget
		self.comboModules = QComboBox()
		self.comboModules.addItems(available_modules)
		self.comboModules.currentIndexChanged.connect(self.updateModuleList)
		self.layout.addWidget(self.comboModules)

		self.search = QLineEdit()
		self.search.textChanged.connect(self.filter_items)
		self.layout.addWidget(self.search)

		layoutLabels = QHBoxLayout()
		self.layout.addLayout(layoutLabels)

		self.labelSelectedClass = QLabel('Selected Class: ')
		self.labelSelectedMemeber= QLabel('Selected Memeber: ')
		layoutLabels.addWidget(self.labelSelectedClass)
		layoutLabels.addWidget(self.labelSelectedMemeber)


		layoutListWidgets = QHBoxLayout()
		self.layout.addLayout(layoutListWidgets)


		self.listWidgetClasses = QListWidget()
		self.listWidgetClasses.verticalScrollBar().setStyleSheet('width: 35px')
		self.listWidgetClasses.itemSelectionChanged.connect(self.updateClassList)
		self.listWidgetClasses.doubleClicked.connect(lambda : self.displayHelper('class'))
		layoutListWidgets.addWidget(self.listWidgetClasses)


		self.listWidgetMemebers = QListWidget()
		self.listWidgetMemebers.verticalScrollBar().setStyleSheet('width: 35px')
		self.listWidgetMemebers.itemSelectionChanged.connect(self.updateMemeberlabel)
		self.listWidgetMemebers.doubleClicked.connect(lambda : self.displayHelper('member'))
		layoutListWidgets.addWidget(self.listWidgetMemebers)

		layoutStatus = QHBoxLayout()

		self.status = QLabel()

		buyMeACoffee = QLabel("Buy Me a Coffee --> " + "<a href=\"https://www.paypal.com/paypalme/jiejenn/5\" style=\"color:#d4fcfb\">Click Me</a>")
		buyMeACoffee.setTextFormat(Qt.RichText)
		buyMeACoffee.setTextInteractionFlags(Qt.TextBrowserInteraction)
		buyMeACoffee.setOpenExternalLinks(True)
		buyMeACoffee.setStyleSheet('color: #ffffff')

		appVersion = QLabel('Created by Jie Jenn (v1.2)')

		layoutStatus.addWidget(self.status)
		layoutStatus.addStretch()
		layoutStatus.addWidget(buyMeACoffee, alignment=Qt.AlignRight)
		layoutStatus.addWidget(appVersion, alignment=Qt.AlignRight)
		self.layout.addLayout(layoutStatus)

		self.setLayout(self.layout)

		self.updateModuleList()

	def displayHelper(self, by_type: str):
		if by_type == 'class':
			class_name = self.listWidgetClasses.currentItem().text()
			obj = getattr(self.module_object, class_name)
		elif by_type == 'member':
			class_name = self.listWidgetClasses.currentItem().text()
			memeber_name = self.listWidgetMemebers.currentItem().text()
			obj = getattr(getattr(self.module_object, class_name), memeber_name)
		else:
			self.status.setText('No information available')
			return

		self.help = HelperText(obj)
		self.help.show()

	def updateMemeberlabel(self):
		try:
			member_name = self.listWidgetMemebers.currentItem().text()
			self.labelSelectedMemeber.setText('Selected Memeber: {0}'.format(member_name))
		except Exception as e:
			self.status.setText(str(e))


	def updateClassList(self):
		self.listWidgetMemebers.clear()

		class_name = self.listWidgetClasses.currentItem().text()

		try:
			obj = getattr(self.module_object, class_name)			
		except AttributeError as e:
			self.status.setText(str(e))
			return 

		self.listWidgetMemebers.addItems(dir(obj))
		self.status.clear()

		try:
			self.labelSelectedClass.setText('Selected Class: {0}'.format(class_name))
		except Excepion as e:
			self.status.setText(str(e))

		
	def updateModuleList(self):
		module_name = self.comboModules.currentText()

		self.module_object = sys.modules.get('PyQt5.' + module_name)
		self.reset_fields()

		if self.module_object is None:
			self.status.setText('Information is not available')
			return

		module_dir = dir(self.module_object)


		self.model = QStringListModel()
		self.model.setStringList(module_dir)

		self.listWidgetClasses.addItems(module_dir)

		self.status.clear()


	def reset_fields(self):
		self.listWidgetClasses.clear()
		self.listWidgetMemebers.clear()
		self.labelSelectedClass.setText('Selected Class: ')
		self.labelSelectedMemeber.setText('Selected Memeber: ')

	def filter_items(self):
		filtered_text = str(self.search.text()).lower()

		if self.model:
			for row in range(self.model.rowCount()):
				if filtered_text in str(self.model.index(row).data()).lower():
					self.listWidgetClasses.setRowHidden(row, False)
				else:
					self.listWidgetClasses.setRowHidden(row, True)


if __name__ == '__main__':
	app = QApplication(sys.argv)


	css_file = QFile(r'dark_theme (4k).css')
	css_file.open(QFile.ReadOnly)
	stream = QTextStream(css_file)

	pyNavigator = PythonNavigator()
	pyNavigator.setStyleSheet(stream.readAll())
	pyNavigator.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')