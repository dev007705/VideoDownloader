from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Dev Downloader"
        self.left = 50
        self.top = 150
        self.width = 600
        self.height = 400
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com/"))
       
        self.show()


app = QApplication(sys.argv)
ex = MainWindow()
sys.exit(app.exec())
