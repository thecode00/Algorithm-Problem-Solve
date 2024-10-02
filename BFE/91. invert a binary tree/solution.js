// https://bigfrontend.dev/problem/invert-a-binary-tree

// This is the type for the node
// type Node = null | {
//   value: number
//   left: Node
//   right: Node
// }

/**
 * @param {Node} node
 * @returns {Node}
 */
function invert(node) {
  if (!node) {
    return node;
  }

  let left = invert(node.left);
  let right = invert(node.right);

  node.right = left;
  node.left = right;
  return node;
}
