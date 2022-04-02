'''
Created on Apr 12, 2014

@author: ABEL
'''

def cheat_outcome(naomi_blocks, ken_blocks):
    return fair_outcome(ken_blocks, naomi_blocks)

def fair_outcome(naomi_blocks, ken_blocks):
    sorted_naomi = sorted(naomi_blocks, reverse=True)
    sorted_ken = sorted(ken_blocks, reverse=True)
    naomi_points = 0

    for n_block in sorted_naomi:
        if len(sorted_ken) == 0:
            break

        if sorted_ken[0] < n_block:
            naomi_points = naomi_points + 1
            sorted_ken.pop()
        elif len(sorted_ken) > 1:
            ken_idx = 1
            while sorted_ken[ken_idx] > n_block:
                ken_idx = ken_idx + 1
            del sorted_ken[ken_idx - 1]

    return naomi_points

def handle_file(infile):
    num_cases = int(infile.readline())
    lines = infile.readlines()

    for i in range(num_cases):
        base_idx = i * 3
        naomi_blocks = [float(e) for e in lines[base_idx + 1].strip().split()]
        ken_blocks = [float(e) for e in lines[base_idx + 2].strip().split()]
        cheat_score = cheat_outcome(naomi_blocks, ken_blocks)
        fair_score = fair_outcome(naomi_blocks, ken_blocks)
        print('Case #{0}: {1} {2}'.format(i + 1, cheat_score, fair_score))

if __name__ == '__main__':
    with open("D-small.in", "r") as f:
        handle_file(f)