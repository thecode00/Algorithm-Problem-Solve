// https://bigfrontend.dev/problem/get-DOM-tree-height

/**
 * @param {HTMLElement | null} tree
 * @return {number}
 */
function getHeight(tree) {
  if (!tree) {
    return 0;
  }

  let maxHeight = 0;
  for (const child of tree.children) {
    maxHeight = Math.max(maxHeight, getHeight(child));
  }

  return maxHeight + 1;
}
