// https://bigfrontend.dev/problem/Reverse-a-linked-list

/**
 * class Node {
 *  new(val: number, next: Node);
 *    val: number
 *    next: Node
 * }
 */

/**
 * @param {Node} list
 * @return {Node}
 */
const reverseLinkedList = (list) => {
  let prev = null;
  while (list) {
    const nextNode = list.next;
    list.next = prev;
    prev = list;
    list = nextNode;
  }

  return prev;
};
