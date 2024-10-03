// https://bigfrontend.dev/problem/two-way-binding

/**
 * @param {{value: string}} state
 * @param {HTMLInputElement} element
 */
function model(state, element) {
  element.value = state.value;

  Object.defineProperty(state, "value", {
    get() {
      return element.value;
    },
    set(value) {
      return (element.value = value);
    },
  });
}
