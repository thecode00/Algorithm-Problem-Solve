// https://bigfrontend.dev/problem/detect-circle-in-linked-list

/**
 * @param {Node} head
 * @return {boolean}
 */
function hasCircle(head) {
  let slow = head,
    fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      return true;
    }
  }
  return false;
}
