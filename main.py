import sys, socket, threading, subprocess, platform, json, traceback, random
from PyQt5.QtWidgets import (QWidget, QFrame, QLabel, QLineEdit, QTextEdit, QGridLayout, QPushButton, QApplication, QInputDialog, QSystemTrayIcon, QTabWidget, QListWidget, QListWidgetItem, QSplitter, QVBoxLayout, QHBoxLayout, QMainWindow, QAction, QDialog, QMenuBar)
from PyQt5 import QtGui, QtWidgets, QtCore, Qt
from PyQt5.QtGui import QIcon, QWindow

class MainClass(QWidget):
    def __init__(self):
        super().__init__()    
        self.initUI()
    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.stockFrame = QFrame()
        self.mainLayout.addWidget(self.stockFrame)
        self.mainButton = QPushButton("Push Me!")
        self.mainLayout.addWidget(self.mainButton)
        self.setLayout(self.mainLayout)


        # self.subjectLabel = QLabel()
        # self.subjectLabel.setAlignment(Qt.Qt.AlignCenter)
        # self.mainLayout.addWidget(self.subjectLabel)
        # self.testLabel = QLabel()
        # self.testLabel.setAlignment(Qt.Qt.AlignCenter)
        # self.mainLayout.addWidget(self.testLabel)
        # self.randomButton = QPushButton("Choose")
        # self.randomButton.clicked.connect(self.randomDef)
        # self.mainLayout.addWidget(self.randomButton)
        # self.setLayout(self.mainLayout)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Stocks")
        self.show()
app = QApplication(sys.argv)
ex = MainClass()
app.exec_()