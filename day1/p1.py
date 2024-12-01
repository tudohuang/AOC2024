def calculate_total_distance(file_path):
    with open(file_path, 'r') as file:
        pairs = [list(map(int, line.split())) for line in file]
        left_list = [pair[0] for pair in pairs]
        right_list = [pair[1] for pair in pairs]


    return sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))


file_path = 'day1/d1.txt'


print(f"總距離: {calculate_total_distance(file_path)}")
