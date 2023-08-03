# https://school.programmers.co.kr/learn/courses/30/lessons/17683

from math import ceil


def convert_time(time):
    return int(time[:2]) * 60 + int(time[3:])


def check_song(song, check_melody, time):
    # 노래를 재생시간만큼 늘림
    song = (song * ceil(time / len(song)))[:time]
    return check_melody in song


def solution(m, musicinfos):
    # 샵음을 처리하기위해 변환
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    for idx, info in enumerate(musicinfos):
        start, end, name, song = info.split(",")
        song = song.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        time = convert_time(end) - convert_time(start)
        musicinfos[idx] = [time, name, song]
    # 노래들중 재생시간이 가장긴걸 반환해야하므로 음수로 변환해서 내림차순정렬을 함, Timsort는 안정정렬이라 입력순서 유지
    musicinfos.sort(key=lambda x: -x[0])

    for time, name, song in musicinfos:
        if check_song(song, m, time):
            return name
    return "(None)"
