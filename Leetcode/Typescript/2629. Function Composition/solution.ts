// https://leetcode.com/problems/function-composition/

type F = (x: number) => number;

function compose(functions: F[]): F {
  return function (x) {
    for (let i = functions.length - 1; i >= 0; i--) {
      x = functions[i](x);
    }
    return x;
  };
}

function compose(functions: F[]): F {
  return (x) => {
    return functions.reduceRight((acc, fn) => fn(acc), x);
  };
}

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
