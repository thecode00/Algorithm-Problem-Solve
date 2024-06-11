// https://school.programmers.co.kr/learn/courses/30/lessons/42884?language=javascript

function solution(routes) {
  routes.sort((a, b) => {
    return a[1] - b[1];
  });
  let cameraPosition = -Infinity,
    cameras = 0;

  for (const [start, end] of routes) {
    // 진입위치가 카메라의 감시위치에서 벗어나면 카메라를 새롭게 추가
    if (start > cameraPosition) {
      cameras += 1;
      cameraPosition = end;
    }
  }
  return cameras;
}
