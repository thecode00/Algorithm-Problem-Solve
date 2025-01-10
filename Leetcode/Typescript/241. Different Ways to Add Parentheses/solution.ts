// https://leetcode.com/problems/different-ways-to-add-parentheses/description/

function diffWaysToCompute(expression: string): number[] {
  if (!isNaN(Number(expression))) {
    return [parseInt(expression)];
  }

  const result: number[] = [];

  for (let idx = 0; idx < expression.length; idx++) {
    if (isNaN(Number(expression[idx]))) {
      const left = diffWaysToCompute(expression.slice(0, idx));
      const right = diffWaysToCompute(
        expression.slice(idx + 1, expression.length)
      );

      for (const l of left) {
        for (const r of right) {
          if (expression[idx] === "-") {
            result.push(l - r);
          } else if (expression[idx] === "+") {
            result.push(l + r);
          } else if (expression[idx] === "*") {
            result.push(l * r);
          }
        }
      }
    }
  }

  return result;
}
