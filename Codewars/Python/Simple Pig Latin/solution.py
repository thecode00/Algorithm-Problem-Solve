# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python


def pig_it(text):
    words = list(text.split())
    for idx, word in enumerate(words):
        # When current word made of alphabet make pig latin
        if word.isalpha():
            words[idx] = word[1:] + word[0] + "ay"
    return " ".join(words)
