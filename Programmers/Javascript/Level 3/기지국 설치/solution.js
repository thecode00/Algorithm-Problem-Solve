// https://school.programmers.co.kr/learn/courses/30/lessons/12979?language=javascript

function solution(n, stations, w) {
  const antenaRange = w * 2 + 1;
  let notCovered = 1,
    answer = 0;

  for (const station of stations) {
    // 기존에 존재하던 안테나의 왼쪽부분에 전파가 안닿는지역이 있는지 확인
    if (notCovered < station - w) {
      answer += Math.ceil((station - w - notCovered) / antenaRange);
    }
    // 헷갈렸던점: 기존에 존재하는 4g기지국도 5g로 바꾸므로 왼쪽에 설치한 안테나의 범위가 기존에 존재하는 안테나의 범위를 넘어갈수 없음
    notCovered = station + w + 1;
  }

  // 마지막으로 마지막 안테나의 오른쪽에 남은부분의 안테나 계산
  if (notCovered <= n) {
    answer += Math.ceil((n - notCovered + 1) / antenaRange);
  }

  return answer;
}
