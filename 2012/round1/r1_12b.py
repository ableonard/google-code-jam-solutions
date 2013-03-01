'''
Created on Apr 27, 2012

@author: Adam
'''

def count_playthroughs(first_stars, second_stars):
	cur_stars = 0
	completions = 0
	
	try:
		passed_level = first_stars.index(cur_stars)
		first_stars[passed_level] = None
		completions = completions + 1
		cur_stars = cur_stars + 1
	except ValueError:
		return completions
	
	while (passed_level >= 0):
		if len(first_stars) > 0:
			try:
				passed_level = first_stars.index(cur_stars)
			except ValueError:
				try:
					passed_level = second_stars.index(cur_stars)
				except ValueError:
					return completions
				else:
					second_stars[passed_level] = None
					completions = completions + 1
					cur_stars = cur_stars + 1
			else:
				first_stars[passed_level] = None
				completions = completions + 1
		else:
			try:
				passed_level = second_stars.index(cur_stars)
				second_stars[passed_level] = None
				completions = completions + 1
			except ValueError:
				return completions

def handle_file(infile):
	num_cases = int(infile.readline())
	
	for i in range(num_cases):
		num_levels = int(infile.readline())
		first_stars = []
		second_stars = []
		
		for j in range(num_levels):
			stars = [int(x) for x in infile.readline().split()]
			first_stars.append(stars[0])
			second_stars.append(stars[1])
		
		completions = count_playthroughs(first_stars, second_stars)
		
		if completions > 0:
			print('Case #{0}: {1}'.format(i + 1, completions))
		else:
			print('Case #{0}: Too Bad'.format(i + 1))

if __name__ == '__main__':
	with open("B-test.in", "r") as f:
		handle_file(f)