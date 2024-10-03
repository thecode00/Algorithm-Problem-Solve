// https://bigfrontend.dev/problem/previous-left-sibling

/**
 * @param {Element} root
 * @param {Element} target
 * @return {Elemnt | null}
 */
function previousLeftSibling(root, target) {
  if (!root) {
    return null;
  }

  let stack = [root];

  while (stack.length > 0) {
    const level = [];
    let prev = null;

    for (const element of stack) {
      if (element === target) {
        return prev;
      }
      prev = element;

      level.push(...element.children);
    }

    stack = level;
  }

  return null;
}

previousLeftSibling();
