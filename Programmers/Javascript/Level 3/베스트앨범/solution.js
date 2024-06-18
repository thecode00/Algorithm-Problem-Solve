// https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=javascript

function solution(genres, plays) {
  const genreAlbums = {}, // 장르별 앨범들
    genreTotalPlay = {}, // 장르별 재생수
    answer = [];

  for (let idx = 0; idx < genres.length; idx++) {
    if (!genreAlbums[genres[idx]]) {
      genreAlbums[genres[idx]] = [];
    }

    if (!genreTotalPlay[genres[idx]]) {
      genreTotalPlay[genres[idx]] = 0;
    }

    genreAlbums[genres[idx]].push([plays[idx], idx]);
    genreTotalPlay[genres[idx]] += plays[idx];
  }

  // 각 장르 앨범들을 재생수, 인덱스순으로 정렬
  for (const key of Object.keys(genreAlbums)) {
    genreAlbums[key].sort((a, b) => {
      if (a[0] > b[0]) {
        return -1;
      }
      if (a[0] < b[0]) {
        return 1;
      }

      return a[1] - b[1];
    });
  }

  // 가장 많이 재생된 장르별로 정렬
  const playInfo = Object.entries(genreTotalPlay);
  playInfo.sort((a, b) => {
    return b[1] - a[1];
  });

  for (const [genre, _] of playInfo) {
    for (let idx = 0; idx < Math.min(genreAlbums[genre].length, 2); idx++) {
      answer.push(genreAlbums[genre][idx][1]);
    }
  }
  return answer;
}
