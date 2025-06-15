// https://leetcode.com/problems/evaluate-reverse-polish-notation/

function evalRPN(tokens: string[]): number {
  const nums: number[] = [];

  for (const t of tokens) {
    if (!isNaN(Number(t))) {
      nums.push(parseInt(t));
    } else {
      const num = nums.pop();

      if (num === undefined) {
        throw new Error("Invalid expression");
      }
      const oper = t;

      switch (oper) {
        case "+":
          nums[nums.length - 1] += num;
          break;
        case "-":
          nums[nums.length - 1] -= num;
          break;
        case "*":
          nums[nums.length - 1] *= num;
          break;
        case "/":
          nums[nums.length - 1] = Math.trunc(nums[nums.length - 1] / num);
          break;
      }
    }
  }

  return nums.pop();
}
