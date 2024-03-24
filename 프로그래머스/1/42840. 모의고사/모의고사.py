def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [sum([a==p[i%len(p)] for i,a in enumerate(answers)]) for p in patterns]
    
    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]