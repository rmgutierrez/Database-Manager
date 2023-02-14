from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    # Set window position and dimensions
    xpos = 200
    ypos = 200
    width = 300
    height = 300
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Test ")

    win.show()
    sys.exit(app.exec_())

window()