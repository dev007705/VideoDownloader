import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QProgressBar, QPushButton
from PyQt5.QtGui import QIcon
from subprocess import call

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Dev Downloader"
        self.left=50
        self.top=150
        self.width=600
        self.height=400
        self.Ui()
        self.show()
        

    def Ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.progress = QProgressBar(self)
        self.progress.setGeometry(30, 40, 200, 25)
        self.openFile()
        #self.btndwn=QPushButton("Download",self)
        #self.btndwn.move(30,80)
        #self.btndwn.clicked.connect(self.openFile)


    def openFile(self):
        options=QFileDialog.Option()
        options |=QFileDialog.DontUseNativeDialog
        file=QFileDialog.getOpenFileName(self,"Open File","All File(*)",options=options)
        if file:
            call("youtube-dl -a vidlist.txt --output '/%(titles)s.%(ext)s'")


if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec())
