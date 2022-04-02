'''
Created on Apr 12, 2014

@author: ABEL
'''

def find_card(first_guess, first_board, second_guess, second_board):
    first_poss = set(first_board[first_guess - 1])
    second_poss = set(second_board[second_guess - 1])
    final_poss = first_poss & second_poss

    if len(final_poss) == 0:
        return 'Volunteer cheated!'
    elif len(final_poss) == 1:
        return final_poss.pop()

    return 'Bad magician!'

def handle_file(infile):
    num_cases = int(infile.readline())
    lines = infile.readlines()
    answers = []

    for i in range(num_cases):
        base_idx = i * 10
        first_guess = int(lines[base_idx].strip())
        first_board = [[int(e) for e in l.split()] for l in lines[base_idx + 1:base_idx + 5]]
        second_guess = int(lines[base_idx + 5].strip())
        second_board = [[int(e) for e in l.split()] for l in lines[base_idx + 6:base_idx + 10]]
        answers.append(find_card(first_guess, first_board, second_guess, second_board))

    for base_idx in range(num_cases):
        print('Case #{0}: {1}'.format(base_idx + 1, answers[base_idx]))

if __name__ == '__main__':
    with open("A-small-attempt1.in", "r") as f:
        handle_file(f)