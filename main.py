import sys, urllib.request, time, random
from matplotlib.finance import date2num
from PyQt5.QtWidgets import (QWidget, QFrame, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtChart import (QCandlestickSeries, QCandlestickSet, QChart, QChartView)
from PyQt5.QtCore import QFile, QDateTime
# from PyQt5 import QtGui, QtWidgets, QtCore, Qt
# from PyQt5.QtGui import QIcon, QWindow

class MainClass(QWidget):
    def __init__(self):
        super().__init__()    
        self.initUI()
    def getStockData(self):
        self.saucePage = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=JBH&interval=1min&apikey=NOC1N35PNDQOFF1A')
        self.msgDialog = QMessageBox()
        self.msgDialog.setText("Downloaded it!")
        self.msgDialog.exec_()
    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.stockFrame = QFrame()
        self.mainLayout.addWidget(self.stockFrame)
        self.mainButton = QPushButton("Push Me!")
        self.mainButton.clicked.connect(self.getStockData)
        self.mainLayout.addWidget(self.mainButton)
        self.setLayout(self.mainLayout)

        self.newSeries = QCandlestickSeries()
        self.newSeries.setName("Test Chart")

        for i in range(1000):

            self.newSet = QCandlestickSet(time.time() * 1000 + (random.randint(-5, 5) * 60000))
            self.newSet.setOpen(random.randint(1, 10))
            self.newSet.setHigh(random.randint(1, 10))
            self.newSet.setLow(random.randint(1, 10))
            self.newSet.setClose(random.randint(1, 10))
            self.newSeries.append(self.newSet)

        # self.newSet2 = QCandlestickSet()
        # self.newSet2.setOpen(1.00)
        # self.newSet2.setHigh(10.00)
        # self.newSet2.setLow(0.50)
        # self.newSet2.setClose(5.00)
        # self.newSeries.append(self.newSet2)

        self.newChart = QChart()
        self.newChart.addSeries(self.newSeries)
        self.newChart.setTitle("Test Actual Chart")
        self.newChart.createDefaultAxes()
        self.newChartView = QChartView(self.newChart)
        self.mainLayout.addWidget(self.newChartView)
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