'''
Created on Apr 12, 2013

@author: ABEL
'''

import math

def is_palindrome(num):
	str_num = str(num)
	length = len(str_num)
	if length % 2 == 0:
		return str_num[0:length // 2] == str_num[:length // 2 - 1:-1]
	else:
		return str_num[0:math.floor(length / 2)] == str_num[:math.floor(length / 2):-1]

def find_fair_squares(inline):
	start, end = [int(n) for n in inline.split()]
	square_count = 0
	
	for j in range(math.ceil(math.sqrt(start)), math.floor(math.sqrt(end)) + 1):
		if is_palindrome(j) and is_palindrome(j * j):
			square_count = square_count + 1
			
	return square_count

def handle_file(infile):
	num_cases = int(infile.readline())
	cases = infile.readlines()
	
	for i in range(num_cases):
		num_squares = find_fair_squares(cases[i].strip())
		print('Case #{0}: {1}'.format(i + 1, num_squares))

if __name__ == '__main__':
	with open("C-large-1.in", "r") as f:
		handle_file(f)