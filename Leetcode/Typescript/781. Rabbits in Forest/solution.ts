// https://leetcode.com/problems/rabbits-in-forest/description

function numRabbits(answers: number[]): number {
  const counter = new Map<number, number>();

  for (const num of answers) {
    counter.set(num, (counter.get(num) || 0) + 1);
  }

  let rabbits = 0;

  for (const [num, count] of counter.entries()) {
    // # Since the answer 'n' means there are n other rabbits of the same color, we add 1 for this rabbit itself.
    const n = num + 1;
    rabbits += n * Math.ceil(count / n);
  }

  return rabbits;
}
