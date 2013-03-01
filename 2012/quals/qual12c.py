'''
Created on Apr 14, 2012

@author: ABEL
'''

def generate_shifts(num_s, case_min_first_s, case_max_first_s):
	shifts = set()
	for x in range(len(num_s) - 1, 0, -1):
		first_digit = num_s[x]
		if (first_digit <= case_max_first_s and first_digit >= case_min_first_s): 
			start = num_s[x:]
			end = num_s[0:x]
			if (start != end and start + end != num_s):
				shifts.add(int(start + end))
	return shifts

def count_recycled(case_min, case_max):
	counter = 0
	counted = []
	case_min_first_s = str(case_min)[0]
	case_max_first_s = str(case_max)[0]
	for x in range(max(case_min, 12), case_max):
		possibles = generate_shifts(str(x), case_min_first_s, case_max_first_s)
		for poss in possibles:
			if (poss <= case_max and poss >= case_min and poss > x):
				counter = counter + 1
				counted.append((x,poss))
	
	return counter

def handle_file(infile):
	num_cases = int(infile.readline())
	lines = infile.readlines()
	
	for i in range(num_cases):
		case_min, case_max = [int(half) for half in lines[i].split()]
		result = count_recycled(case_min, case_max)
		print('Case #{0}: {1}'.format(i + 1, result))

if __name__ == '__main__':
	with open("C-large.in", "r") as f:
		handle_file(f)