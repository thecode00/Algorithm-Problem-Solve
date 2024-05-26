// https://school.programmers.co.kr/learn/courses/30/lessons/258711

function solution(edges) {
  // [진입 차수, [연결되어있는 노드 리스트]]
  const nodeInfo = {};

  for (const [a, b] of edges) {
    if (!nodeInfo[a]) {
      nodeInfo[a] = [0, []];
    }

    if (!nodeInfo[b]) {
      nodeInfo[b] = [0, []];
    }

    nodeInfo[a][1].push(b);
    nodeInfo[b][0] += 1;
  }

  const answer = [0, 0, 0, 0];
  let totalGraph = 0;

  // 그래프의 개수는 진입 노드에 연결되어있는 노드 수
  for (const node in nodeInfo) {
    const indgr = nodeInfo[node][0],
      outdgrNum = nodeInfo[node][1].length;
    if (indgr === 0 && outdgrNum >= 2) {
      answer[0] = parseInt(node);
      totalGraph = outdgrNum;
    } else if (indgr >= 1 && outdgrNum === 0) {
      // 막대 그래프
      answer[2] += 1;
    } else if (indgr >= 1 && outdgrNum >= 2) {
      // 8자 그래프
      answer[3] += 1;
    }
  }

  // 도넛 그래프
  answer[1] = totalGraph - answer[2] - answer[3];

  return answer;
}
