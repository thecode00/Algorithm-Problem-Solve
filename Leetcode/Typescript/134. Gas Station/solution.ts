// https://leetcode.com/problems/gas-station/description/

function canCompleteCircuit(gas: number[], cost: number[]): number {
  let totalGas = 0,
    totalCost = 0;

  for (let idx = 0; idx < gas.length; idx++) {
    totalGas += gas[idx];
    totalCost += cost[idx];
  }

  if (totalGas < totalCost) {
    return -1;
  }

  let curGas = 0;
  let start = 0;
  for (let idx = 0; idx < gas.length; idx++) {
    curGas += gas[idx] - cost[idx];
    if (curGas < 0) {
      start = idx + 1;
      curGas = 0;
    }
  }

  return start;
}
