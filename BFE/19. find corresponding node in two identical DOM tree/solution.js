// https://bigfrontend.dev/problem/find-corresponding-node-in-two-identical-DOM-tree

/**
 * @param {HTMLElement} rootA
 * @param {HTMLElement} rootB - rootA and rootB are clone of each other
 * @param {HTMLElement} nodeA
 */
const findCorrespondingNode = (rootA, rootB, target) => {
  if (rootA === target) {
    return rootB;
  }

  for (let idx = 0; idx < rootA.children.length; idx++) {
    const result = findCorrespondingNode(
      rootA.children[idx],
      rootB.children[idx],
      target
    );
    if (result) {
      return result;
    }
  }
};
