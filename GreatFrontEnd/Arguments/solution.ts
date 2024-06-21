// https://www.greatfrontend.com/questions/javascript/count-by

export default function countBy<T>(
  array: Array<T>,
  iteratee: (value: T) => number | string
): Record<string, number> {
  const result: Record<string, number> = {};

  array.forEach((data) => {
    const iterData = iteratee(data);
    if (!result[iterData]) {
      result[iterData] = 0;
    }
    result[iterData] += 1;
  });

  return result;
}