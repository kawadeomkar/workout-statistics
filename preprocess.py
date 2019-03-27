# Omkar Kawade
# preproceess data/data.rtf 

# takes in a filename and returns list of individual workout sessions
def dataSrc(filename):
	data = ''
	with open(filename, 'r') as workout_data:
		data = workout_data.read()
		data = data.split('\n\n')
	return data
	

if __name__ == '__main__':
	# dictionary containing all workout statistics
	workouts = {}
	filename = 'data/data.txt'
	data = dataSrc(filename)

	for day in data:
		day = day.split('\n')
		if day[0] == '' and len(day) > 3:
			newMuscleGroup = day[1].split(' ')
			date, muscle = newMuscleGroup[0], newMuscleGroup[1]
			max_weight = 0.0
			for exercise in day[3:len(day)]:
				set = ((exercise.split(' '))[1]).split('x')
				reps, weight = int(set[0]), float(set[1])
				if weight > max_weight and reps >= 3:
					max_weight = weight
			if muscle not in workouts.keys():
				workouts[muscle] = {}
			workouts[muscle][date] = max_weight

	# test results for chest
	for day, weight in workouts['chest'].items():
		print(day, weight)

