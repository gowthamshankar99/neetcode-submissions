from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max, max_student = 0, ""
    for score in scores:
        name, ind_score = score
        if ind_score > max:
            max = ind_score
            max_student = name
    
    return max_student




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
