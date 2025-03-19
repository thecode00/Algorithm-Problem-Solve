// https://leetcode.com/problems/find-if-path-exists-in-graph/description/

function validPath( // Union find
  n: number,
  edges: number[][],
  source: number,
  destination: number
): boolean {
  const union = new UnionFind(n);

  for (const [u, v] of edges) {
    union.union(u, v);
  }

  return union.findParent(source) === union.findParent(destination);
}

class UnionFind {
  parent: number[];

  constructor(n: number) {
    this.parent = Array.from({ length: n }, (_, i) => i);
  }

  union(a: number, b: number) {
    const pA = this.findParent(a);
    const pB = this.findParent(b);

    if (pA > pB) {
      this.parent[pA] = pB;
    } else {
      this.parent[pB] = pA;
    }
  }

  findParent(n: number): number {
    if (this.parent[n] !== n) {
      this.parent[n] = this.findParent(this.parent[n]);
    }
    return this.parent[n];
  }
}

function validPath( // BFS
  n: number,
  edges: number[][],
  source: number,
  destination: number
): boolean {
  const graph: number[][] = Array.from({ length: n }, (_) => []);

  for (const [u, v] of edges) {
    graph[u].push(v);
    graph[v].push(u);
  }

  const visited = Array.from({ length: n }, (_) => false);

  const stack: number[] = [source];

  while (stack.length > 0) {
    const curNode = stack.pop();

    if (curNode === destination) {
      return true;
    }

    for (const nextNode of graph[curNode]) {
      if (!visited[nextNode]) {
        stack.push(nextNode);
        visited[nextNode] = true;
      }
    }
  }

  return false;
}
