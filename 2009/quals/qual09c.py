'''
Created on Sep 3, 2009

@author: Adam Leonard
'''

def processString(file):
	cases = int(file.readline())
	
	results = []
	
	for i in range(cases):
		num = findCodeJam(file.readline().strip())
		print("Case #{0!s}: {1!s:0>4}".format(i+1, num))
		results.append(num)
	
	#with open('C-large.out', 'w') as f:
	#	for i in range(len(results)):
	#		f.write("Case #{0!s}: {1!s:0>4}\n".format(i+1, results[i]))
			
def findCodeJam(test_string):
	return findStringRecur(test_string, 'welcome to code jam')
		
def findStringIter(test_string, search_char):
	indices = []
	index = 0
	index = test_string.find(search_char, index)
	
	while index > -1:
		indices.append(index)
		index = test_string.find(search_char, index + 1)
		
	return indices

def findStringRecur(test_string, search_string):
	#print('Test:<{0}>, Search:<{1}>'.format(test_string, search_string))
	
	if search_string == '':
		return 1
	elif test_string == '' or \
	 len(test_string) < len(search_string) or \
	 not set(test_string).issuperset(set(search_string)):
		return 0
	
	search_char = search_string[0]
	index = test_string.find(search_char)
	total = 0
		
	while index > -1:
		#print('Test:<{0}>, Search:<{1}>'.format(test_string, search_string))
		#print('Index at {0!s}, recursing. Total={1!s}'.format(index,total))
		total = (total + findStringRecur(test_string[index + 1:], search_string[1:])) % 10000
		#print('Returning from recursion, total=' + str(total))
		index = test_string.find(search_char, index + 1)
		
	return total

if __name__ == '__main__':
	with open("C-large.in") as f:
		processString(f)