// https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=javascript

function solution(progresses, speeds) {
  const answer = [];

  while (progresses.length > 0) {
    // 첫번째 작업이 완료될때까지 걸리는 날짜
    const firstProgressDayCount = Math.ceil((100 - progresses[0]) / speeds[0]);

    for (let idx = 0; idx < progresses.length; idx++) {
      progresses[idx] += firstProgressDayCount * speeds[idx];
    }

    // 첫번째 작업과 같이 배포할수있는 작업개수를 구함
    let doneProgresses = 0;
    for (let idx = 0; idx < progresses.length; idx++) {
      if (progresses[idx] < 100) {
        break;
      }
      doneProgresses += 1;
    }

    progresses = progresses.slice(doneProgresses);
    speeds = speeds.slice(doneProgresses);
    answer.push(doneProgresses);
  }
  return answer;
}
