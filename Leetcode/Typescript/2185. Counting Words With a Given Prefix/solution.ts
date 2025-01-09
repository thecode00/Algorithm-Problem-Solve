// https://leetcode.com/problems/counting-words-with-a-given-prefix/description

// RegExp
function prefixCount(words: string[], pref: string): number {
  let count = 0;
  const reg = new RegExp(`^${pref}+`);

  for (const word of words) {
    if (reg.test(word)) {
      count += 1;
    }
  }

  return count;
}

// Bruteforce
function prefixCount(words: string[], pref: string): number {
  let count = 0;

  for (const word of words) {
    if (word.length < pref.length) {
      continue;
    }

    let isPrefix = true;
    for (let idx = 0; idx < pref.length; idx++) {
      if (word[idx] !== pref[idx]) {
        isPrefix = false;
        break;
      }
    }

    count += isPrefix ? 1 : 0;
  }

  return count;
}

function prefixCount(words: string[], pref: string): number {
  let count = 0;

  for (const word of words) {
    if (word.startsWith(pref)) {
      count += 1;
    }
  }

  return count;
}
