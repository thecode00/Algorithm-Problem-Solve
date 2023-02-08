# https://school.programmers.co.kr/learn/courses/30/lessons/17680


from collections import deque


def solution(cacheSize, cities):
    time = 0
    # cacheSizr와 cities개수의 최대값이 30, 100000이므로 배열로 구현해도 상관없지만 딕셔너리를 같이사용해봄
    cache_city = {}
    cache = deque()

    for city in cities:
        city = city.lower()
        if city in cache_city:  # Set에 캐싱된 도시를 찾아봄
            cache.remove(city)
            cache.append(city)
            time += 1
            continue

        time += 5
        if cacheSize == 0:  # 캐시사이즈가 0이면 캐싱작업을 안하고 넘어감
            continue
        if len(cache) == cacheSize:
            del cache_city[cache.popleft()]
        cache_city[city] = 1
        cache.append(city)
    return time


def solution(cacheSize, cities):
    time = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:   # Set이 아닌 배열이므로 O(cacheSize)의 시간복잡도를 가짐
            cache.remove(city)
            time += 1
        else:
            time += 5
        cache.append(city)
    return time
