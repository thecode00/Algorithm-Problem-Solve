# https://dmoj.ca/problem/ccc08j2

from collections import deque
import sys

input = sys.stdin.readline

playlist = deque(["A", "B", "C", "D", "E"])

while True:
    button = input().strip()
    press_count = int(input())

    if button == "4":
        print(" ".join(playlist))
        break

    for _ in range(press_count):
        if button == "1":
            playlist.append(playlist.popleft())
        elif button == "2":
            playlist.appendleft(playlist.pop())
        elif button == "3":  # Swap song
            playlist[0], playlist[1] = playlist[1], playlist[0]
