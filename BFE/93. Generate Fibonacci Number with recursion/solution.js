// https://bigfrontend.dev/problem/Generate-Fibonacci-Number-with-recursion

// please modify code below to make it work for large number like `fib(1000)`
// recursion should still be used
const dp = [0, 1];
function fib(n) {
  if (n <= 1) {
    return n;
  }
  if (dp[n]) {
    return dp[n];
  }
  dp.push(fib(n - 1) + fib(n - 2));
  return dp[n];
}
