// https://leetcode.com/problems/reconstruct-itinerary/description/

function findItinerary(tickets: string[][]): string[] {
  let airport = new Map<string, string[]>();

  for (const airline of tickets) {
    const from = airline[0],
      to = airline[1];

    if (!airport.has(from)) {
      airport.set(from, []);
    }
    airport.get(from).push(to);
  }

  for (const array of airport.values()) {
    array.sort().reverse();
  }

  const stack = ["JFK"];
  const path: string[] = [];
  while (stack.length > 0) {
    const cur = stack[stack.length - 1];

    if (!airport.has(cur) || airport.get(cur).length === 0) {
      path.push(cur);
      stack.pop();
      continue;
    }

    stack.push(airport.get(cur).pop());
  }
  return path.reverse();
}
