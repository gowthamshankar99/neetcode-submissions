from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=helper, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=helper_number)
    return numbers

def helper(word: str):
    return len(word)

def helper_number(number: int):
    return abs(number)    


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
