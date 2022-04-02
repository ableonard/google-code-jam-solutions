def init_maze(dimension, lydia_path):
    maze = [['X' for i in range(dimension)] for j in range(dimension)]
    coords = [0, 0]
    
    for step in lydia_path:
        if step == 'S':
            maze[coords[0]][coords[1]] = 'S'
            coords[1] += 1
        elif step == 'E':
            maze[coords[0]][coords[1]] = 'E'
            coords[0] += 1

    return maze


def find_path(maze):
    coords = [0, 0]
    max_pos = len(maze) -  1
    path = []

    while coords[0] < max_pos or coords[1] < max_pos:
        if maze[coords[0]][coords[1]] == 'S':
            path.append('E')
            coords[0] += 1
        elif maze[coords[0]][coords[1]] == 'E': 
            path.append('S')
            coords[1] += 1
        elif path[-1] == 'S':
            path.append('E')
            coords[0] += 1
        else:
            path.append('S')
            coords[1] += 1

    return ''.join(path)


def handle_input():
    num_cases = int(input())

    for i in range(num_cases):
        dimension = int(input())
        lydia_path = input()
        maze = init_maze(dimension, lydia_path)
        my_path = find_path(maze)
        print('Case #{0}: {1}'.format(i + 1, my_path))

if __name__ == '__main__':
    handle_input()
