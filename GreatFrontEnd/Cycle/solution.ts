// https://www.greatfrontend.com/questions/javascript/cycle

export default function cycle<T>(...values: Array<T>): () => T {
  let index = 0;

  return () => {
    index %= values.length;
    return values[index++];
  };
}
