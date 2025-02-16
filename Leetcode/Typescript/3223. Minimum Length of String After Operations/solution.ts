// https://leetcode.com/problems/minimum-length-of-string-after-operations/description

// Optimized count char amount
function minimumLength(s: string): number {
  const A_CODE = "a".charCodeAt(0);
  const charCount = Array.from({ length: 26 }, (_) => 0);

  for (let idx = 0; idx < s.length; idx++) {
    charCount[s.charCodeAt(idx) - A_CODE] += 1;
  }

  let minimumLength = 0;

  for (const count of charCount) {
    if (count === 0) {
      continue;
    }

    minimumLength += count % 2 === 0 ? 2 : 1;
  }

  return minimumLength;
}

function minimumLength(s: string): number {
  const counter = new Map<string, number>();
  let minimumLength = 0;

  for (const char of s) {
    counter.set(char, (counter.get(char) || 0) + 1);

    if (counter.get(char) === 3) {
      counter.set(char, 1);
    }
  }

  for (const count of counter.values()) {
    minimumLength += count;
  }

  return minimumLength;
}
