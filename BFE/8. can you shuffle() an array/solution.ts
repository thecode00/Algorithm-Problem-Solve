// https://bigfrontend.dev/problem/can-you-shuffle-an-array

// This is a JavaScript coding problem from BFE.dev

function shuffle(arr: any[]): void {
  // Fisher–Yates shuffle
  for (let idx = arr.length - 1; idx > 0; idx--) {
    const picked = Math.floor(Math.random() * (idx + 1));
    [arr[idx], arr[picked]] = [arr[picked], arr[idx]];
  }
}
