// https://bigfrontend.dev/problem/implement-a-simple-DOM-wrapper-to-support-method-chaining-like-jQuery

/**
 * @param {HTMLElement} el - element to be wrapped
 */
function $(el) {
  return new Wrapper(el);
}

class Wrapper {
  constructor(el) {
    this.el = el;
  }

  css(property, value) {
    this.el.style[property] = value;
    return this;
  }
}
