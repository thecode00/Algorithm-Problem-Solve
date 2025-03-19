// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     left: _Node | null
 *     right: _Node | null
 *     next: _Node | null
 *     constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function connect(root: _Node | null): _Node | null {
  if (!root) {
    return null;
  }

  const linkNode: _Node[] = [];

  function search(root: _Node | null, level: number) {
    if (!root) {
      return;
    }

    if (linkNode.length === level) {
      linkNode.push(new _Node());
    }
    linkNode[level].next = root;
    linkNode[level] = root;

    search(root.left, level + 1);
    search(root.right, level + 1);
  }

  search(root, 0);

  return root;
}
