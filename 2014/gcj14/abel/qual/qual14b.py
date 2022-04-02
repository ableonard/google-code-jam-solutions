'''
Created on Apr 12, 2014

@author: ABEL
'''

def calc_best_time(farm_cost, farm_production, total_amount):
    total_time = 0
    prod_per_sec = 2.0
    time_remaining = total_amount / prod_per_sec
    time_for_farm = farm_cost / prod_per_sec
    time_with_farm = time_for_farm + (total_amount / (prod_per_sec + farm_production))

    while time_remaining > time_with_farm:
        total_time = total_time + time_for_farm
        prod_per_sec = prod_per_sec + farm_production
        time_remaining = total_amount / prod_per_sec
        time_for_farm = farm_cost / prod_per_sec
        time_with_farm = time_for_farm + (total_amount / (prod_per_sec + farm_production))

    return total_time + time_remaining

def handle_file(infile):
    num_cases = int(infile.readline())
    lines = infile.readlines()

    for i in range(num_cases):
        setup_data = lines[i].strip().split()
        farm_cost = float(setup_data[0])
        farm_production = float(setup_data[1])
        total_amount = float(setup_data[2])
        answer = calc_best_time(farm_cost, farm_production, total_amount)
        print('Case #{0}: {1:0.7f}'.format(i + 1, answer))

if __name__ == '__main__':
    with open("B-large.in", "r") as f:
        handle_file(f)