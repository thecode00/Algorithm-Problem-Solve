// https://leetcode.com/problems/course-schedule/description/

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const require = new Map<number, number[]>();
  const indegree = new Array(numCourses).fill(0);

  for (const courses of prerequisites) {
    const from = courses[0],
      to = courses[1];

    if (!require.has(to)) {
      require.set(to, []);
    }
    require.get(to)!.push(from);
    indegree[from] += 1;
  }

  const stack: number[] = [];
  for (let idx = 0; idx < numCourses; idx++) {
    if (indegree[idx] === 0) {
      stack.push(idx);
    }
  }

  while (stack.length > 0) {
    const cur = stack.pop();

    if (!require.has(cur)) {
      continue;
    }
    for (const course of require.get(cur)) {
      indegree[course] -= 1;
      if (indegree[course] === 0) {
        stack.push(course);
      }
    }
  }

  for (const course of indegree) {
    if (course !== 0) {
      return false;
    }
  }

  return true;
}

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  // Count completed courses
  const indegree = Array(numCourses).fill(0);
  const graph = new Map<number, number[]>();

  for (const [end, start] of prerequisites) {
    indegree[end] += 1;
    if (!graph.has(start)) {
      graph.set(start, []);
    }
    graph.get(start).push(end);
  }

  const stack = [];
  for (let idx = 0; idx < numCourses; idx++) {
    if (indegree[idx] === 0) {
      stack.push(idx);
    }
  }

  let complete = 0;

  while (stack.length > 0) {
    const cur = stack.pop();
    complete += 1;
    if (!graph.has(cur)) {
      continue;
    }
    for (const nextCourse of graph.get(cur)) {
      indegree[nextCourse] -= 1;
      if (indegree[nextCourse] === 0) {
        stack.push(nextCourse);
      }
    }
  }

  return complete === numCourses;
}
