// https://bigfrontend.dev/problem/find-the-first-duplicate-character-in-a-string

/**
 * @param {string} str
 * @return {string | null}
 */
function firstDuplicate(str) {
  const used = new Set();

  for (const char of str) {
    if (used.has(char)) {
      return char;
    }
    used.add(char);
  }

  return null;
}
