'''
Created on May 8, 2010

@author: ABEL
'''

def on_or_off(snappers, snaps):
	lit_at = 2 ** snappers - 1
	
	if snaps < lit_at:
		return "OFF"
	elif ((snaps - lit_at) % (lit_at + 1)) != 0:
		return "OFF"
	
	return "ON"

def handleFile(infile):
	test_cases = int(infile.readline())
	
	for i in range(test_cases):
		snappers, snaps = map(int, infile.readline().split())
		print("Case #{0}: {1}".format(i + 1, on_or_off(snappers, snaps)))

if __name__ == '__main__':
	with open("A-large.in", "r") as f:
		handleFile(f)