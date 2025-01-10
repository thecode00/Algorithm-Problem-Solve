// https://leetcode.com/problems/sort-list/description/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function sortList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) {
    return head;
  }

  // Split linkedlist
  let slow = head,
    fast = head;
  let prev = null;

  while (fast && fast.next) {
    fast = fast.next.next;
    prev = slow;
    slow = slow.next;
  }

  prev.next = null;

  const l1 = sortList(head),
    l2 = sortList(slow);
  return mergeNode(l1, l2);
}

function mergeNode(l1, l2) {
  if (!l1) {
    return l2;
  }
  if (!l2) {
    return l1;
  }

  if (l1.val > l2.val) {
    const temp = l1;
    l1 = l2;
    l2 = temp;
  }

  l1.next = mergeNode(l1.next, l2);
  return l1;
}
