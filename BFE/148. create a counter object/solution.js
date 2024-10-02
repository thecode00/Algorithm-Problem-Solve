// https://bigfrontend.dev/problem/create-a-counter-object

/**
 * @returns { {count: number}}
 */
function createCounter() {
  return {
    _counter: 0,
    get count() {
      return this._counter++;
    },
  };
}
