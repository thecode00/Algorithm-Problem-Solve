// https://www.greatfrontend.com/questions/javascript/type-utilities-ii

export function isArray(value: unknown): boolean {
  return value instanceof Array;
}

export function isFunction(value: unknown): boolean {
  return value instanceof Function;
}

export function isObject(value: unknown): boolean {
  return value instanceof Object;
}

export function isPlainObject(value: unknown): boolean {
  if (value == null) {
    return false;
  }
  return (
    Object.getPrototypeOf(value) === null ||
    Object.getPrototypeOf(value) === Object.prototype
  );
}
