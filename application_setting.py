import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSettings
 
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
 
        self.settings = QSettings('MyQtApp', 'App1')
        # print(self.settings.fileName())
        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            pass
 
    def closeEvent(self, event):
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())
 
app = QApplication(sys.argv)        
 
demo = MyApp()
demo.show()
 
sys.exit(app.exec_())