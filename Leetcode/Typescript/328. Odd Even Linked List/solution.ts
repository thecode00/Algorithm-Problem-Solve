// https://leetcode.com/problems/odd-even-linked-list/description/

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

function oddEvenList(head: ListNode | null): ListNode | null {
  const evenList = new ListNode(),
    oddList = new ListNode();
  let evenCur = evenList,
    oddCur = oddList,
    index = 1;

  while (head) {
    if (index % 2 == 0) {
      evenCur.next = head;
      evenCur = evenCur.next;
    } else {
      oddCur.next = head;
      oddCur = oddCur.next;
    }

    head = head.next;
    index += 1;
  }

  evenCur.next = null;
  oddCur.next = evenList.next;

  return oddList.next;
}
