# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python


def two_sum(numbers, target):
    index_dict = dict()
    for idx, num in enumerate(numbers):
        if target - num in index_dict:  # If target - num in numbers return index
            return [index_dict[target - num], idx]
        index_dict[num] = idx
    return []
