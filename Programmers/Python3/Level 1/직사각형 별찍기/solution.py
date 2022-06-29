# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print("*" * a)
