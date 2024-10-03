// https://bigfrontend.dev/problem/count-function

// IIFE closure
const count = (() => {
  let counter = 0;

  const func = () => ++counter;
  func["reset"] = () => {
    counter = 0;
  };

  return func;
})();
