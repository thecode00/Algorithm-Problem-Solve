// https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=javascript

function solution(record) {
  const userInfo = new Map(),
    printCommands = [],
    answer = [];

  record.forEach((data, idx) => {
    const [command, userId, nickName] = data.split(" ");
    switch (command) {
      case "Enter":
        userInfo.set(userId, nickName);
        printCommands.push(["Enter", userId]);
        break;
      case "Leave":
        printCommands.push(["Leave", userId]);
        break;
      case "Change":
        userInfo.set(userId, nickName);
        break;
    }
  });

  for (const [command, userId] of printCommands) {
    switch (command) {
      case "Enter":
        answer.push(`${userInfo.get(userId)}님이 들어왔습니다.`);
        break;
      case "Leave":
        answer.push(`${userInfo.get(userId)}님이 나갔습니다.`);
        break;
    }
  }
  return answer;
}
