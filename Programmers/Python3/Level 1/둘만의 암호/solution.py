# https://school.programmers.co.kr/learn/courses/30/lessons/155652


def solution(s, skip, index):
    skip = set(skip)
    result = []
    for char in s:
        ascii_char = ord(char)
        plus = index
        while plus > 0:
            # a의 아스키코드가 97이므로 현재 아스키코드에서 1을 더한값에서 97을뺀후 알파벳 개수인 26 나머지연산을 함
            ascii_char = (ascii_char + 1 - 97) % 26 + 97
            if chr(ascii_char) not in skip:  # skip에 현재 알파벳이 없을때만 plus 숫자를 줄임
                plus -= 1
        result.append(chr(ascii_char))

    return "".join(result)
