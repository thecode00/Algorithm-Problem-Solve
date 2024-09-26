// https://leetcode.com/problems/daily-temperatures/description/

function dailyTemperatures(temperatures: number[]): number[] {
  const weatherStack: number[] = [],
    result: number[] = Array(temperatures.length).fill(0);

  for (let idx = 0; idx < temperatures.length; idx++) {
    while (
      weatherStack.length > 0 &&
      temperatures[weatherStack[weatherStack.length - 1]] < temperatures[idx]
    ) {
      const recordIndex = weatherStack.pop();
      result[recordIndex!] = idx - recordIndex!;
    }
    weatherStack.push(idx);
  }

  return result;
}
