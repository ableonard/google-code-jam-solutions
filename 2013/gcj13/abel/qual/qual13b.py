'''
Created on Apr 13, 2013

@author: ABEL
'''

def check_pattern(lawn):
	return ''

def handle_file(infile):
	num_cases = int(infile.readline())
	lines = infile.readlines()
	lawns = []
	line_idx = 0
	for i in range(num_cases):
		height, _ = [int(l) for l in lines[line_idx].strip().split()]
		lawns.append([])
		for j in range(height):
			lawns[i].append(lines[line_idx + j])
		line_idx = line_idx + height + 1
	
	for i in range(num_cases):
		possible = check_pattern(lawns[i])
		print('Case #{0}: {1}'.format(i + 1, possible))

if __name__ == '__main__':
	with open("B-small-attempt1.in", "r") as f:
		handle_file(f)