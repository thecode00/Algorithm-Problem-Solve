// https://www.greatfrontend.com/questions/javascript/min-by

export default function minBy<T>(
  array: Array<T>,
  iteratee: (value: T) => any
): any {
  let min = undefined,
    minValue = null;

  array.map((e) => {
    if (!iteratee(e)) {
      return;
    }

    if (minValue === null || iteratee(e) < minValue) {
      min = e;
      minValue = iteratee(e);
    }
  });

  return min;
}
