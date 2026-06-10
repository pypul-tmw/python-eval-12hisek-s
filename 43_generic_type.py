"""
In addition to basic types like str, int, and float, you can also use generic types in your type hints. 
For example, you might use a list of ints:
"""
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)

print(sum_list([1,2,3,4]))


def count_words(words: list[str]) -> dict[str,int]:
    word_counts={}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print(count_words([
    "apple",
    "banana",
    "apple",
    "orange",
    "banana"
]))