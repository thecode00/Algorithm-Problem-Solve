# https://dmoj.ca/problem/ecoo17r1p1

import sys

input = sys.stdin.readline

price = [12, 10, 7, 5]
for _ in range(10):
    cost = int(input())
    ratio = list(map(float, input().split()))
    total_students = int(input())
    students = [int(total_students * r) for r in ratio]
    # Any missing or extra people should be removed from or added to the group with the highest percentage of attendees
    students[students.index(max(students))] += total_students - sum(students)
    total = 0
    for p, s in zip(price, students):
        total += p * s

    if total / 2 >= cost:
        print("NO")
    else:
        print("YES")
