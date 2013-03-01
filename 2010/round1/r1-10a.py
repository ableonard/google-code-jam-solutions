'''
Created on May 22, 2010

@author: ABEL
'''

import re

def how_many_mkdirs(exdirs, newdirs):
	exdirs.sort(reverse=True)
	newdirs.sort()
	regexes = [re.compile('^' + re.escape(x) + '$') for x in exdirs]
	mkdirs = 0
	
	for newdir in newdirs:
		pathelems = newdir.split('/')
		for i in range(len(pathelems) - 1, 0, -1):
			checked_path = '/'.join(pathelems[0:i + 1])
			matchingpatterns = [regex for regex in regexes if re.match(regex, checked_path)]
			if (len(matchingpatterns) > 0):
				break;
			else:
				mkdirs = mkdirs + 1
				regexes.append(re.compile('^' + checked_path + '$'))
				
	return mkdirs

def handleFile(infile):
	test_cases = int(infile.readline())
	
	for i in range(test_cases):
		numexdirs, numnewdirs = map(int, infile.readline().split())
		exdirs = []
		for j in range(numexdirs):
			exdirs.append(infile.readline().strip())
		newdirs = []
		for k in range(numnewdirs):
			newdirs.append(infile.readline().strip())
		print("Case #{0}: {1}".format(i + 1, how_many_mkdirs(exdirs, newdirs)))

if __name__ == '__main__':
	with open("A-large.in", "r") as f:
		handleFile(f)