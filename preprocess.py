# Omkar Kawade
# preproceess data/data.rtf 

FILE_NAME = 'data/data.txt'
OUT_FILE = 'data/processed.txt'

def saveData(workouts): 
	global OUT_FILE
	
	with open(OUT_FILE, 'w') as outfile:
		for muscle in workouts.keys():
			outfile.write(muscle)
			for exercise, stats in workouts[muscle].items():
				outfile.write(exercise)
				for day, weight in workouts[muscle][exercise].items():
					outfile.write(str(day) + " " + str(weight))
			outfile.write("---")


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
	rest_days = {}
	# helper variables
	previous_muscle = ''
	previous_date = ''

	data = dataSrc(FILE_NAME)
	
	# loop through each split workout	
	for day in data:
		day = day.split('\n')
		# check if the row is a new workout
		if day[0] == '' and len(day) > 3:
			newMuscleGroup = day[1].split(' ')
			exercise_name = day[2]
			date, muscle = newMuscleGroup[0], newMuscleGroup[1]
			
			# find max weight in sub list 
			max_weight = 0.0
			for exercise in day[3:len(day)]:
				set = ((exercise.split(' '))[1]).split('x')
				reps, weight = int(set[0]), float(set[1])
				if weight > max_weight and reps >= 3:
					max_weight = weight

			# create new dictionary within workouts dictionary if muscle DNE
			if muscle not in workouts.keys():
				workouts[muscle] = {}
			# create new dictionary within workouts[muscle] if exercise name DNE
			if exercise_name not in workouts[muscle].keys():
				workouts[muscle][exercise_name] = {}
			# set the date equal to max_weight of set
			workouts[muscle][exercise_name][date] = max_weight
			previous_muscle, previous_date = muscle, date
		
		# handle rest days
		elif day[0] == '' and day[1].split(' ')[1] == 'rest':
			splits = day[1].split(' ')
			date, reason = splits[0], ''
			if len(splits) > 2 and splits[2] != '':
				reason = splits[2]
			rest_days[date] = reason				

		# continuing workout exercisees
		elif len(day) > 1 and day[1].split(" ")[1] != 'rest':
			exercise_name = day[0]
			# find max weight in sub list
			max_weight = 0.0
			for exercise in day[1:len(day)]:
				set = ((exercise.split(' '))[1]).split('x')
				reps, weight = int(set[0]), float(set[1])
				if weight > max_weight and reps >= 3:
					max_weight = weight
			# create new dictionary within workouts[muscle] if exercise name DNE
			if exercise_name not in workouts[previous_muscle].keys():
				workouts[previous_muscle][exercise_name] = {}
			workouts[previous_muscle][exercise_name][previous_date] = max_weight
	
	saveData(workouts)
	print(rest_days)	
