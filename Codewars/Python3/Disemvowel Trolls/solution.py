# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python


def disemvowel(string_):
    vowels = {"a", "e", "i", "o", "u"}
    # List of exclude vowels
    s = [char for char in string_ if char.lower() not in vowels]
    return "".join(s)
