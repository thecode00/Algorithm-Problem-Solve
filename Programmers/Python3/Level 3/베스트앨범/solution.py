# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict


def solution(genres, plays):
    answer = []
    song_dict = defaultdict(list)  # 기본값이 []인 딕셔너리
    play_dict = defaultdict(int)  # 기본값이 0인 딕셔너리

    for idx, value in enumerate(genres):
        play = plays[idx]
        song_dict[value].append([play, idx])  # [플레이 수, 곡의 인덱스]
        play_dict[value] += play

    for key in song_dict.keys():
        song_dict[key].sort(key=lambda x: -x[0])
    # play수 별로 정렬한 장르 리스트
    genre = sorted(play_dict.keys(), key=lambda x: -play_dict[x])

    for g in genre:
        for idx in range(2):
            try:
                answer.append(song_dict[g][idx][1])
            except:
                break

    return answer
