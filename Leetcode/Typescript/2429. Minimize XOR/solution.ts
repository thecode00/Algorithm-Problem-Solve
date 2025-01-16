// https://leetcode.com/problems/minimize-xor/description

function minimizeXor(num1: number, num2: number): number {
  const num1Bits = numOfBits(num1);
  const num2Bits = numOfBits(num2);
  let diffBits = num1Bits - num2Bits;
  let answer = num1;

  // num1 bits < num2 bits, to minimize XOR remove LSB
  if (diffBits > 0) {
    let fillIndex = 0;

    while (diffBits > 0) {
      while ((answer & (1 << fillIndex)) === 0) {
        fillIndex += 1;
      }

      diffBits -= 1;
      answer ^= 1 << fillIndex;
    }
  }
  // num1 bits >= num2 bits, num1 XOR num2 = 0, replace a non-1 bit with a 1 bit
  else {
    let blankIndex = 0;

    while (diffBits < 0) {
      while (answer & (1 << blankIndex)) {
        blankIndex += 1;
      }

      diffBits += 1;
      answer ^= 1 << blankIndex;
    }
  }

  return answer;
}

function numOfBits(num: number): number {
  let count = 0;

  while (num > 0) {
    count += num & 1;
    num >>= 1;
  }

  return count;
}
