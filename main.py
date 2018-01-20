import sys, urllib.request, time, random, json, collections, datetime
from PyQt5.QtWidgets import (QWidget, QFrame, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QMessageBox, QLineEdit, QLabel)
from PyQt5.QtChart import (QCandlestickSeries, QCandlestickSet, QChart, QChartView)
from PyQt5.QtCore import QFile, QDateTime
# from PyQt5 import QtGui, QtWidgets, QtCore, Qt
# from PyQt5.QtGui import QIcon, QWindow

class MainClass(QWidget):
    def __init__(self):
        super().__init__()    
        self.initUI()
    def getStockData(self):
        self.close()
        print("HI")

        self.mainLayout.removeWidget(self.newChartView)
        self.newSeries = QCandlestickSeries()
        self.newSeries.setName("Test Chart 2")

        self.saucePage = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + self.stockRequestBox.text() + '&interval=1min&apikey=NOC1N35PNDQOFF1A')
        self.output = self.saucePage.read()
        self.webContent = self.output.decode('utf-8') # Convert from bytes to string


        self.writePage = open('stock.json', 'w') # Write webContent to a html file because otherwise i can't use readlines()
        self.writePage.write(self.webContent) # It's very efficient code trust me
        self.writePage.close()

        self.sauce = json.load(open('stock.json'))

        # print(sauce["Monthly Time Series"]["2018-01-14 20:23:00"]["1. open"])
        self.openStocks = {}
        for date in self.sauce["Monthly Time Series"]:
            self.openStocks[date] = self.sauce["Monthly Time Series"][date]["1. open"]

        self.ordered = collections.OrderedDict(sorted(self.openStocks.items()))
        for k, v in self.ordered.items():
            dateString = k
            dt = datetime.datetime(int(dateString[:4]), int(dateString[5:7]), int(dateString[8:10]))
            
            self.newSet = QCandlestickSet((time.mktime(dt.timetuple()) * 1000))
            self.newSet.setOpen(float(v))
            self.newSet.setHigh(float(self.sauce["Monthly Time Series"][k]["2. high"]))
            self.newSet.setLow(float(self.sauce["Monthly Time Series"][k]["3. low"]))
            self.newSet.setClose(float(self.sauce["Monthly Time Series"][k]["4. close"]))
            self.newSeries.append(self.newSet)
        self.newChart = QChart()
        self.newChart.addSeries(self.newSeries)
        self.newChart.setTitle("Test Actual Chart")
        self.newChart.createDefaultAxes()
        self.newChartView = QChartView(self.newChart)
        self.mainLayout.addWidget(self.newChartView)
        self.show()

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.stockFrame = QFrame()
        self.mainLayout.addWidget(self.stockFrame)
        self.mainButton = QPushButton("Push Me!")
        self.mainButton.clicked.connect(self.getStockData)
        self.mainLayout.addWidget(self.mainButton)

        self.stockRequestLayout = QHBoxLayout()
        self.stockRequestedLabel = QLabel("Stock: ")
        self.stockRequestLayout.addWidget(self.stockRequestedLabel)
        self.stockRequestBox = QLineEdit()
        self.stockRequestLayout.addWidget(self.stockRequestBox)

        self.mainLayout.addLayout(self.stockRequestLayout)
        self.setLayout(self.mainLayout)

        self.newSeries = QCandlestickSeries()
        self.newSeries.setName("Test Chart")

        # for i in range(1000):

        #     self.newSet = QCandlestickSet(time.time() * 1000 + (random.randint(-5, 5) * 60000))
        #     self.newSet.setOpen(random.randint(1, 10))
        #     self.newSet.setHigh(random.randint(1, 10))
        #     self.newSet.setLow(random.randint(1, 10))
        #     self.newSet.setClose(random.randint(1, 10))
        #     self.newSeries.append(self.newSet)

        # self.newSet2 = QCandlestickSet()
        # self.newSet2.setOpen(1.00)
        # self.newSet2.setHigh(10.00)
        # self.newSet2.setLow(0.50)
        # self.newSet2.setClose(5.00)
        # self.newSeries.append(self.newSet2)


        self.saucePage = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=BHP&apikey=NOC1N35PNDQOFF1A')
        
        self.output = self.saucePage.read()
        self.webContent = self.output.decode('utf-8') # Convert from bytes to string


        self.writePage = open('stock.json', 'w') # Write webContent to a html file because otherwise i can't use readlines()
        self.writePage.write(self.webContent) # It's very efficient code trust me
        self.writePage.close()

        self.sauce = json.load(open('stock.json'))

        # print(sauce["Monthly Time Series"]["2018-01-14 20:23:00"]["1. open"])
        self.openStocks = {}
        for date in self.sauce["Monthly Time Series"]:
            self.openStocks[date] = self.sauce["Monthly Time Series"][date]["1. open"]

        self.ordered = collections.OrderedDict(sorted(self.openStocks.items()))
        count = 0
        for k, v in self.ordered.items():
            dateString = k
            dt = datetime.datetime(int(dateString[:4]), int(dateString[5:7]), int(dateString[8:10]))
            
            self.newSet = QCandlestickSet((time.mktime(dt.timetuple()) * 1000))
            self.newSet.setOpen(float(v))
            self.newSet.setHigh(float(self.sauce["Monthly Time Series"][k]["2. high"]))
            self.newSet.setLow(float(self.sauce["Monthly Time Series"][k]["3. low"]))
            self.newSet.setClose(float(self.sauce["Monthly Time Series"][k]["4. close"]))
            self.newSeries.append(self.newSet)
            count = count + 1
            # if count > 8:
            #     break



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