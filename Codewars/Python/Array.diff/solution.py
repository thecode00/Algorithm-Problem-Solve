# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    b_elements = set(b)
    result = []
    for num in a:
        if num not in b_elements:
            result.append(num)
    return result
