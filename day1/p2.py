from collections import Counter

def calculate_similarity_score(file_path):
    with open(file_path, 'r') as file:
        pairs = [list(map(int, line.split())) for line in file]
    

        left_list = [pair[0] for pair in pairs]
        right_list = [pair[1] for pair in pairs]
    
    right_counts = Counter(right_list)
    

    similarity_score = sum(num * right_counts[num] for num in left_list)
    return similarity_score


file_path = 'day1/d1.txt'


print(f"相似度得分: {calculate_similarity_score(file_path)}")
