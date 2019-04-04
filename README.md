# Workout Statistics (under construction)
Workout statistics done right, implemented in Python.

---
## Dependencies 
- Scikit-learn
- Matplotlib

## Input file template
The input text file must be of .txt format and located in the data folder of the main directory. The input file must be named "data.txt" but can be changed with the global variable "FILE_NAME" in preprocess.py. 

At the beginning of the data file, the first line contains 'Workout Statistics'. Afterwards there is a space and then a workout is included. The date and muscle group is included, followed by each exercise and their respective set and rep by weight count. An example is shown below; feel free to look at the data.txt file as well for reference.


example:
> Workout Statistics
> 
> 3/5 shoulder&triceps 
> Shoulder press
> 1 10x25
> 1 5x30
> 2 5x35
> 1 4x35
>
> Triceps pull down 
> 2 8x40
> 1 7x35
> 
> 
> ... (2 line gap -> next workout)

## 
