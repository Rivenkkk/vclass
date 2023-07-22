from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow_1 import Ui_Dialog_1
from mainwindow_2 import Ui_Dialog_2
import time
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog_1()
        self.ui.setupUi(self)
        self.ui_connection()
        
    def ui_connection(self):
        self.setIDButton = self.ui.setIDButton
        
        self.setIDButton.clicked.connect(self.buttonClick)
        
    def buttonClick(self):
        self.widget = QWidget() # or whatever your top-level class is
        self.ui = Ui_Dialog_2()
        self.ui.setupUi(self.widget)
        self.widget.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

