'''
Created on May 22, 2010

@author: ABEL
'''

def pure_sets(n):
	

def handleFile(infile):
	test_cases = int(infile.readline())
	
	for i in range(test_cases):
		n = int(infile.readline())
		print("Case #{0}: {1}".format(i + 1, pure_sets(n)))

if __name__ == '__main__':
	with open("C-small.in", "r") as f:
		handleFile(f)