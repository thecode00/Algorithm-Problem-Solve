// https://bigfrontend.dev/problem/create-a-browser-history

class BrowserHistory {
  /**
   * @param {string} url
   * if url is set, it means new tab with url
   * otherwise, it is empty new tab
   */
  constructor(url) {
    this.stack = [];
    this.pointer = 0;
    if (url) {
      this.stack.push(url);
    }
  }
  /**
   * @param { string } url
   */
  visit(url) {
    this.pointer += 1;
    this.stack[this.pointer] = url;
  }

  /**
   * @return {string} current url
   */
  get current() {
    return this.stack[this.pointer];
  }

  // go to previous entry
  goBack() {
    this.pointer = Math.max(this.pointer - 1, 0);
  }

  // go to next visited url
  forward() {
    this.pointer = Math.min(this.pointer + 1, this.stack.length - 1);
  }
}
