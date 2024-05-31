// https://school.programmers.co.kr/learn/courses/30/lessons/17680?language=javascript

function solution(cacheSize, cities) {
  if (cacheSize === 0) {
    return cities.length * 5;
  }

  let cache = [],
    time = 0;
  const cacheSet = new Set();
  for (let city of cities) {
    city = city.toLowerCase();

    // 캐시에 저장되어있는 도시들 확인
    if (cacheSet.has(city)) {
      // Cache hit
      cache = cache.filter((c) => {
        return c !== city;
      });

      if (cache.length < cacheSize) {
        cache.push(city);
      }
      time += 1;
    } else {
      // Cache miss
      cacheSet.add(city);
      if (cache.length >= cacheSize) {
        cacheSet.delete(cache[0]);
        cache.shift();
      }
      cache.push(city);
      time += 5;
    }
  }
  return time;
}
