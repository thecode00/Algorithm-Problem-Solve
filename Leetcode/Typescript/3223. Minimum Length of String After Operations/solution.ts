// https://leetcode.com/problems/minimum-length-of-string-after-operations/description

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
