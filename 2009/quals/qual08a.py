'''
Created on Aug 19, 2009

@author: ABEL (Adam Leonard)
'''

names = []
queries = []

def queryHandler(file):
	cases = int(file.readline())
	for i in range(cases):
		engines = int(file.readline())
		for i in range(engines):
			names.append(str(file.readline()))
		numqueries = int(file.readline())
		for i in range(numqueries):
			queries.append(str(file.readline()))
		switches = distributeQueries()
		print "Case #" + str(i) + ": " + str(switches)

def distributeQueries():
	current = ''
	 for query in queries:
	 	if 


if __name__ == '__main__':
	with open("A-small.in") as f:
		queryHandler(f)