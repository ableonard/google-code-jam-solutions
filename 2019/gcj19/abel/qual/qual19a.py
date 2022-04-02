def four_to_two(string_of_end_num):
    return int(string_of_end_num.replace('4', '2'))

def find_addends(end_num):
    first_addend = four_to_two(str(end_num))
    second_addend = end_num - first_addend
    return [first_addend, second_addend]

def handle_input():
    num_cases = int(input())
    answers = []

    for i in range(num_cases):
        end_num = int(input())
        first, second = find_addends(end_num)
        print('Case #{0}: {1} {2}'.format(i + 1, first, second))

if __name__ == '__main__':
    handle_input()
