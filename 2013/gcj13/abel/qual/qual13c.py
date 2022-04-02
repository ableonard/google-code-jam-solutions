'''
Created on Apr 12, 2013

@author: ABEL
'''

import math

cache = []

def is_palindrome(num):
	str_num = str(num)
	length = len(str_num)
	if length % 2 == 0:
		return str_num[0:length // 2] == str_num[:length // 2 - 1:-1]
	else:
		return str_num[0:math.floor(length / 2)] == str_num[:math.floor(length / 2):-1]

def handle_file(infile):
	global cache
	num_cases = int(infile.readline())
	cases = infile.readlines()
	bot = 999999999999
	top = 0
	
	for i in range(num_cases):
		start, end = [int(n) for n in cases[i].split()]
		cases[i] = [start, end]
		if start < bot:
			bot = start
		if end > top:
			top = end
			
	cache = [is_palindrome(i) and is_palindrome(i * i) for i in range(math.ceil(math.sqrt(bot)), math.floor(math.sqrt(top)) + 1)]
	
	for i in range(num_cases):
		print('Case #{0}: {1}'.format(i + 1, len([1 for n in cache[math.ceil(math.sqrt(cases[i][0])):math.floor(math.ceil(cases[i][1]))] if n])))

if __name__ == '__main__':
	with open("C-large-1.in", "r") as f:
		handle_file(f)