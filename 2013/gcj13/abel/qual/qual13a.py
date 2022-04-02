'''
Created on Apr 13, 2013

@author: ABEL
'''

def check_board(board):
	xw = set(['X','T'])
	ow = set(['O', 'T'])
	
	r1 = set(board[0])
	r2 = set(board[1])
	r3 = set(board[2])
	r4 = set(board[3])
	c1 = set([board[0][0], board[1][0], board[2][0], board[3][0]])
	c2 = set([board[0][1], board[1][1], board[2][1], board[3][1]])
	c3 = set([board[0][2], board[1][2], board[2][2], board[3][2]])
	c4 = set([board[0][3], board[1][3], board[2][3], board[3][3]])
	d1 = set([board[0][0], board[1][1], board[2][2], board[3][3]])
	d2 = set([board[0][3], board[1][2], board[2][1], board[3][0]])
	
	a = [r1, r2, r3, r4, c1, c2, c3, c4, d1, d2]
	
	for state in a:
		if state <= xw:
			return 'X won'
		elif state <= ow:
			return 'O won'
		
	if '.' not in board[0] and '.' not in board[1] and '.' not in board[2] and '.' not in board[3]:
		return 'Draw'
	
	return 'Game has not completed'

def handle_file(infile):
	num_cases = int(infile.readline())
	lines = infile.readlines()
	boards = []
	for i in range(num_cases):
		board_idx = i * 5
		boards.append([lines[board_idx].strip(), lines[board_idx + 1].strip(), lines[board_idx + 2].strip(), lines[board_idx + 3].strip()])
	
	for i in range(num_cases):
		outcome = check_board(boards[i])
		print('Case #{0}: {1}'.format(i + 1, outcome))

if __name__ == '__main__':
	with open("A-large.in", "r") as f:
		handle_file(f)