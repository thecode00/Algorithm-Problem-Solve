// https://bigfrontend.dev/problem/create-a-simple-store-for-DOM-node

class NodeStore {
  constructor() {
    this.newMap = {};
  }
  /**
   * @param {Node} node
   * @param {any} value
   */
  set(node, value) {
    this.newMap[node] = value;
  }
  /**
   * @param {Node} node
   * @return {any}
   */
  get(node) {
    return this.newMap[node];
  }

  /**
   * @param {Node} node
   * @return {Boolean}
   */
  has(node) {
    return node in this.newMap;
  }
}
