# analysis.py
# take processed data and analyze results using matplotlib, scikit
import matplotlib.pyplot as plt

PROCESSED_FILE_NAME = 'data/processed.txt'

# plot bench press improvement
def plotBenchPress():
	temp = ''

def readProcessedData():
	global PROCESSED_FILE_NAME
	
	data = ''
	with open(PROCESSED_FILE_NAME, 'r') as processed_data:
		data = processed_data.read()
		data = data.split('---')
	return data

if __name__ == '__main__':
	data = readProcessedData()
	print(data)
