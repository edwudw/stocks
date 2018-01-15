import json, urllib.request, collections

# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()


saucePage = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=JBH&interval=1min&apikey=NOC1N35PNDQOFF1A') # Download html file from website
output = saucePage.read()
webContent = output.decode('utf-8') # Convert from bytes to string


writePage = open('stock.json', 'w') # Write webContent to a html file because otherwise i can't use readlines()
writePage.write(webContent) # It's very efficient code trust me
writePage.close()

sauce = json.load(open('stock.json'))

# print(sauce["Time Series (1min)"]["2018-01-14 20:23:00"]["1. open"])
openStocks = {}
for date in sauce["Time Series (1min)"]:
	openStocks[date] = sauce["Time Series (1min)"][date]["1. open"]

ordered = collections.OrderedDict(sorted(openStocks.items()))
for k, v in ordered.items(): print(k + ": " + v)
