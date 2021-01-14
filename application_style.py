# The available PyQt styles may differ system to system, 
# but because many people install the PyQt binary the styles installed are often the same. 
# You can get a list of available styles using the Python interpreter, like so:
# $ python3
# >>> import PyQt5.QtWidgets
# >>> print(PyQt5.QtWidgets.QStyleFactory.keys())
# ['Windows', 'Fusion']

"""Grid layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

# The default style of PyQt is called 'Fusion'
app.setStyle('Windows')
# app.setStyle('Fusion')

window = QWidget()
window.setWindowTitle('Application Style')
layout = QGridLayout()
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
layout.addWidget(button1, 0, 0)
layout.addWidget(button2, 0, 1)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())