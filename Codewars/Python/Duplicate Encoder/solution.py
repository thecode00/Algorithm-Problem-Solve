# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python


from collections import Counter


def duplicate_encode(word):
    word = word.lower()  # Change all upper letter to lower letter
    count = Counter(word)  # Count number of letters
    result = []
    for s in word:  # Encode letter
        if count[s] > 1:
            result.append(")")
        else:
            result.append("(")
    return "".join(result)
