// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

class FindElements {
  elementSet = new Set<number>();
  root: TreeNode | null;

  constructor(root: TreeNode | null) {
    this.root = root;
    this.init();
  }

  find(target: number): boolean {
    return this.elementSet.has(target);
  }

  init() {
    if (!this.root) {
      return;
    }

    const stack: TreeNode[] = [this.root];
    this.root.val = 0;

    while (stack.length > 0) {
      let cur = stack.pop();
      this.elementSet.add(cur.val);

      if (cur.left) {
        cur.left.val = cur.val * 2 + 1;
        stack.push(cur.left);
      }
      if (cur.right) {
        cur.right.val = cur.val * 2 + 2;
        stack.push(cur.right);
      }
    }
  }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */
