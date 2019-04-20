# analysis.py
# take processed data and analyze results using matplotlib, scikit
#import matplotlib.pyplot as plt

PROCESSED_FILE_NAME = 'data/processed.txt'

# plot bench press improvement
def plotBenchPress():
	temp = ''

def processData(data):
	ret = []
	for workout in data:
		workout = workout.split('\n')
		print(workout)	

def readData():
	global PROCESSED_FILE_NAME
	
	data = ''
	with open(PROCESSED_FILE_NAME, 'r') as processed_data:
		data = processed_data.read()
		data = data.split('---')
	return data

if __name__ == '__main__':
	data = readData()
	processData(data)
