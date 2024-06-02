// https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=javascript

function solution(n, computers) {
  const visited = Array(n).fill(false);
  let answer = 0;

  // 한 네트워크에 연결되있는 컴퓨터를 DFS로 탐색
  for (let idx = 0; idx < n; idx++) {
    if (!visited[idx]) {
      visited[idx] = true;
      const stack = [idx];

      while (stack.length > 0) {
        const cur = stack.pop();

        for (let next = 0; next < n; next++) {
          if (computers[cur][next] && !visited[next]) {
            stack.push(next);
            visited[next] = true;
          }
        }
      }

      answer += 1;
    }
  }
  return answer;
}
